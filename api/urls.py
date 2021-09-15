from django.urls import path, include
from rest_framework import urlpatterns
from .views import PostView, PostCategoryView, PostDetailView

urlpatterns= [
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', PostView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<str:category>/', PostCategoryView.as_view(), name='post_category')
]
