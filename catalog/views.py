from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


# def index(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Продукты'
#     }
#     return render(request, 'catalog/index.html', context)

class ProductsListView(ListView):
    model = Product
    extra_context = {'title': 'Продукты'}


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'Продукт {product_item.name}'
#     }
#     return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html/'

