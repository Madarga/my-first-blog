from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import Post 

class PostList(TemplateView):
    template_name = 'blog/post_list.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, self.template_name, {'posts':posts})

class PostDetail(TemplateView):
    template_name = 'blog/post_detail.html'
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        return render(request, self.template_name, {'post':post})

class PostEdit(TemplateView):
    template_name = 'blog/post_edit.html'
    
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
            

class PostNew(TemplateView):
    template_name = 'blog/post_edit.html'
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, self.template_name, {'form': form})