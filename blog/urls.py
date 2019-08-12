from django.urls import path
from blog.views import PostList
from blog.views import PostDetail
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/detail', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/detail/edit', PostDetail.as_view(), name='post_edit'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]