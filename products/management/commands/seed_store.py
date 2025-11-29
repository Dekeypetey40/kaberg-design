from __future__ import annotations

import random
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Iterable, List, Tuple

from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction
from django.utils.text import slugify

from products.models import Category, Product

# --------- config ---------
PARENTS_TO_CHILDREN: Dict[str, Tuple[str, ...]] = {
    "home_decoration": ("lamps", "garden", "cushions", "kitchen_bath"),
    "for_children": ("toys", "kitchen", "bedroom"),
    "antique": ("pottery", "fabrics", "lighting"),
}

PLACEHOLDER_IMAGE_URLS: Tuple[str, ...] = (
    # picsum and placehold are stable placeholders
    "https://picsum.photos/seed/{seed}/800/800",
    "https://placehold.co/800x800?text={seed}",
)

ADJECTIVES = [
    "Elegant", "Cozy", "Vintage", "Modern", "Classic", "Deluxe",
    "Handmade", "Premium", "Compact", "Eco", "Artisan", "Soft",
]
NOUNS = [
    "Lamp", "Rug", "Vase", "Cushion", "Toy Set", "Bedspread",
    "Mixer", "Tea Set", "Garden Light", "Wall Art", "Pottery Bowl",
    "Fabric Roll", "Desk Light", "Kids Plate", "Pillow",
]

# --------- helpers ---------
def money(amount: float) -> Decimal:
    return Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def unique_slug(base: str, existing: Iterable[str]) -> str:
    base_slug = slugify(base)[:180] or "item"
    slug = base_slug
    suffix = 2
    while slug in existing:
        slug = f"{base_slug}-{suffix}"
        suffix += 1
    return slug

@dataclass
class CreatedCounts:
    categories: int = 0
    products: int = 0

# --------- command ---------
class Command(BaseCommand):
    help = "Seed categories and generate demo products."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--per-category",
            type=int,
            default=6,
            help="Products to create per leaf category (default: 6).",
        )
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing products before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **opts) -> None:
        per_category: int = int(opts["per_category"])
        reset: bool = bool(opts["reset"])

        counts = CreatedCounts()

        if reset:
            deleted, _ = Product.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Deleted {deleted} products."))

        # 1) Ensure categories tree exists
        parent_objs: Dict[str, Category] = {}
        for parent_slug, children in PARENTS_TO_CHILDREN.items():
            parent_obj, _ = Category.objects.get_or_create(
                slug=parent_slug,
                defaults={
                    "name": parent_slug.replace("_", " ").title(),
                    "description": f"{parent_slug.replace('_', ' ').title()} collection.",
                },
            )
            parent_objs[parent_slug] = parent_obj
            counts.categories += 1

            for child_slug in children:
                child_obj, _ = Category.objects.get_or_create(
                    slug=child_slug,
                    defaults={
                        "name": child_slug.replace("_", " ").title(),
                        "parent_category": parent_obj,
                        "description": f"{child_slug.replace('_', ' ').title()} items.",
                    },
                )
                counts.categories += 1

        # 2) Create products per leaf category
        leaf_categories: List[Category] = list(
            Category.objects.filter(parent_category__isnull=False)
        )

        existing_slugs = set(Product.objects.values_list("slug", flat=True))

        for cat in leaf_categories:
            for i in range(per_category):
                # random-ish name that maps to category
                adjective = random.choice(ADJECTIVES)
                noun = random.choice(NOUNS)
                base_name = f"{adjective} {noun} ({cat.name})"
                slug = unique_slug(base_name, existing_slugs)
                existing_slugs.add(slug)

                price = money(random.uniform(9, 299))
                rating = Decimal(str(round(random.uniform(3.0, 5.0), 1)))
                stock = random.randint(0, 50)

                seed = f"{slug[:20]}{i}"
                image_url_template = random.choice(PLACEHOLDER_IMAGE_URLS)
                image_url = image_url_template.format(seed=seed)

                Product.objects.create(
                    category=cat,
                    name=base_name,
                    slug=slug,
                    description=(
                        f"Demo product for {cat.name}. "
                        f"Quality: {adjective.lower()}. Perfect as a {noun.lower()}."
                    ),
                    stock=stock,
                    price=price,
                    rating=rating,
                    image_url=image_url,
                )
                counts.products += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeding complete: {counts.categories} categories ensured, "
                f"{counts.products} products created."
            )
        )
