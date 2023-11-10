from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductsListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('contacts/', contacts, name='contact'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='view_product')
]