from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post 

#Dapat kung iclick ang blog title kay iredirect siya sa post_detail.html na page

class PostList(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts':posts})

class PostDetail(TemplateView):
    def post(self, request, *args, **kwargs):
        template_name = 'blog/post_detail.html'
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect(self.template_name, pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form':form})



  