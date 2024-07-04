from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models import Product


# Create your views here.


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'blog/product-detail.html', context)
