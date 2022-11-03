from django.urls import path
from .views import BlogPostListView, BlogPostCategoryView, BlogPostDetailView, BlogPostFeaturedView, index

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('image', index, name='index'),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
    ]
