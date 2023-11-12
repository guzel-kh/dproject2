from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, \
    PostUpdateView, PostDeleteView, PostCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('', PostListView.as_view(), name='post_list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
