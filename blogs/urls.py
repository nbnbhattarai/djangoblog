from django.urls import path
from .views import HomePage, BlogView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:blog_id>/', BlogView.as_view(), name='blog_info'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:blog_id>/', BlogUpdateView.as_view(), name='blog_update'),
]