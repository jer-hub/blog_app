from django.urls import path
from .views import create_post, view_blog, edit_post, delete_post


app_name='blog'
urlpatterns = [
    path('<int:id>/', view_blog, name='view-blog'),
    path('create-post/', create_post, name='create-post'),
    path('post/<int:id>/edit/', edit_post, name='edit-post'),
    path('post/<int:id>/delete/', delete_post, name='delete-post'),
]