from django.shortcuts import render
from django.views import generic
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import  authenticate, login
from django.views.generic import  View

from posts.models import Post
from .models import Post
from django.utils import timezone

from django.db.models import Q, QuerySet


# from templates.posts import post_form.html

def post_list(request):

    blog_post = Post.objects.all()
    query = request.GET.get("q")
    if query:
        blog_post = blog_post.filter(Q(title__icontains=query)|
                                    Q(content__icontains=query)).distinct()
    paginator = Paginator(blog_post, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    all_posts = paginator.get_page(page)


    return render(request, 'blog/index.html', {'all_posts': all_posts})


class Detailview(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'




class PostCreate(CreateView):


    model = Post
    fields = ['title', 'content', 'post_image']
    # template_name = 'blog/post_form.html'

    success_url = reverse_lazy('post:index')



