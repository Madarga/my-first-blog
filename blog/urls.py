from django.views.generic import TemplateView
from django.urls import path
from blog.views import PostList
from blog.views import PostDetail
from blog.views import PostEdit
from blog.views import PostNew
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('post/new/', PostNew.as_view(), name='post_new'),
]