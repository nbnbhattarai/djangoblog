from django.urls import path
from .views import HomePage, BlogView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:pk>/', BlogView.as_view(), name='blog_info'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]