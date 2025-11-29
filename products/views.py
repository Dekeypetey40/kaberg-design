from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import ProductForm
from .models import Category, Product, Favorites

# Top-level groups used by your dropdowns
TOP_LEVEL = {"home_decoration", "antique", "for_children"}


def product_detail(request, product_id: int):
    """Show a single product."""
    product = get_object_or_404(Product.objects.select_related("category"), pk=product_id)
    return render(request, "products/product_detail.html", {"product": product})


def all_products_view(request, category_slug: str | None = None):
    """
    List products with optional:
      - category filter (?category=lamps) OR top-level group (?category=home_decoration)
      - search (?q=chair)
      - sort (?sort=price&direction=asc|desc, or sort=name|category)
    """
    products = Product.objects.select_related("category").all()
    total_products = Product.objects.count()

    # -------- category filtering
    slug = request.GET.get("category") or category_slug
    if slug:
        if slug in TOP_LEVEL:
            products = products.filter(category__parent_category__slug=slug)
        else:
            products = products.filter(category__slug=slug)

    # -------- search
    q = (request.GET.get("q") or "").strip()
    if q:
        products = products.filter(Q(name__icontains=q))

    # -------- sort
    sort = request.GET.get("sort")
    direction = request.GET.get("direction", "asc")
    if sort:
        if sort == "name":
            products = products.annotate(lower_name=Lower("name"))
            sort_key = "lower_name"
        elif sort == "category":
            sort_key = "category__name"
        else:
            sort_key = sort
        if direction == "desc":
            sort_key = f"-{sort_key}"
        products = products.order_by(sort_key)

    # Show the three main groups in the badge row
    current_categories = Category.objects.filter(parent_category__isnull=True).order_by("name")

    context = {
        "products": products,
        "search_term": q,
        "current_categories": current_categories,
        "current_sorting": f"{sort}_{direction}" if sort else "",
        "total_products": total_products,
    }
    return render(request, "products/products.html", context)


@login_required
def add_product(request):
    """Create a new product (superusers only)."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect("product_detail", product.id)
        messages.error(request, "Failed to add product. Please ensure the form is valid.")
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})


@login_required
def edit_product(request, product_id: int):
    """Edit a product (superusers only)."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        messages.error(request, "Please ensure the form is valid.")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    return render(request, "products/edit_product.html", {"form": form, "product": product})


@login_required
def delete_product(request, product_id: int):
    """Delete a product (superusers only)."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def add_to_favorites(request, product_id: int):
    """Toggle product in the user's favorites."""
    product = get_object_or_404(Product, pk=product_id)
    favorite_qs = Favorites.objects.filter(product=product, user=request.user)

    if favorite_qs.exists():
        favorite_qs.first().delete()
    else:
        Favorites.objects.create(user=request.user, product=product)
        messages.success(request, "Thanks for liking our product!")

    return redirect(reverse("products"))
