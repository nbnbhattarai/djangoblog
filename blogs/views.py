from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django import views
from django.urls import reverse

from .models import Blog
from .forms import BlogForm

class HomePage(views.View):
    def get(self, request):
        blogs = Blog.objects.all()
        # print('blogs: ', blogs)
        context = {
            'blogs': blogs,
        }
        return render(request, 'homepage.html', context)


class BlogView(views.View):
    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        context = {
            'blog': blog,
        }
        return render(request, 'blog.html', context)


class BlogCreateView(views.View):
    def get(self, request):
        form = BlogForm()
        context = {
            'form': form,
        }
        return render(request, 'blog_create.html', context)

    def post(self, request):
        form = BlogForm(request.POST)
        
        if form.is_valid():
            print('form is valid')
            blog = form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print('form is not valid')
            context = {
                'form': form,
            }

            return render(request, 'blog_create.html', context)

class BlogUpdateView(views.View):
    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        # blog.delete()
        # return HttpResponseRedirect(reverse('home'))
        form = BlogForm(instance=blog)
        context = {
            'form': form,
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        form = BlogForm(request.POST, instance=blog)
        
        if form.is_valid():
            print('form is valid')
            blog = form.save()
            return HttpResponseRedirect(reverse('blog_info', args=[blog_id]))
        else:
            print('form is not valid')
            context = {
                'form': form,
            }

            return render(request, 'blog_create.html', context)
