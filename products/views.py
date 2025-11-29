from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Favorites
from .forms import ProductForm


def product_detail(request, product_id):
    """ A view to show individual products with additional info """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def all_products_view(request, category_slug=None):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    total_products = Product.objects.count()

    # Sorting
    sort = request.GET.get("sort")
    direction = request.GET.get("direction")
    if sort:
        sortkey = sort
        if sort == "name":
            products = products.annotate(lower_name=Lower("name"))
            sortkey = "lower_name"
        elif sort == "category":
            sortkey = "category__name"
        if direction == "desc":
            sortkey = f"-{sortkey}"
        products = products.order_by(sortkey)

    # Category filter — only filter when a category is provided
    category_slug = request.GET.get("category")
    if category_slug:
        # Top-level groupings (use parent_category)
        if category_slug in {"home_decoration", "antique", "for_children"}:
            products = products.filter(category__parent_category__slug=category_slug)
        else:
            products = products.filter(category__slug=category_slug)

    # Search (independent of category)
    query = request.GET.get("q", "").strip()
    if "q" in request.GET:
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect("products")
        products = products.filter(Q(name__icontains=query))

    current_sorting = f"{sort or ''}_{direction or ''}"

    # Always provide a safe, iterable value (or just [] if you don’t need it)
    current_categories = list(
        Category.objects.filter(parent_category__isnull=True).order_by("name")
    )

    context = {
        "products": products,
        "search_term": query or None,
        "current_categories": current_categories,
        "current_sorting": current_sorting,
        "total_products": total_products,
    }
    return render(request, "products/products.html", context)


@login_required
def add_product(request):
    """ Add a product to the store if admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect('product_detail', product.id)
        else:
            messages.error(request,
                           'Failed to add product.\
                               Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_to_favorites(request, product_id):
    """
    Toggles a product as a favorite if user is logged in
    """
    product = get_object_or_404(Product, pk=product_id)
    favorite = Favorites.objects.filter(product=product, user=request.user)

    if favorite.exists():
        favorite = favorite.first()
        favorite.delete()
    else:
        favorite = Favorites.objects.create(user=request.user,
                                            product=product)
        messages.success(request, 'Thanks for liking our product!')
    return redirect(reverse('products'))
