from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django import views
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login

from .models import Blog
from .forms import BlogForm


class HomePage(ListView):
    model = Blog
    template_name = 'homepage.html'


# class HomePageBak(views.View):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         # print('blogs: ', blogs)
#         context = {
#             'blogs': blogs,
#         }
#         return render(request, 'homepage.html', context)


class BlogView(DetailView):
    model = Blog
    template_name = 'blog.html'

# class BlogViewBak(views.View)
#     def get(self, request, blog_id):
#         blog = get_object_or_404(Blog, id=blog_id)
#         context = {
#             'blog': blog,
#         }
#         return render(request, 'blog.html', context)



class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ('title', 'content',)


# class BlogCreateViewBak(views.View):
#     def get(self, request):
#         form = BlogForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'blog_create.html', context)

#     def post(self, request):
#         form = BlogForm(request.POST)
        
#         if form.is_valid():
#             print('form is valid')
#             blog = form.save()
#             return HttpResponseRedirect(reverse('home'))
#         else:
#             print('form is not valid')
#             context = {
#                 'form': form,
#             }

#             return render(request, 'blog_create.html', context)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ('title', 'content',)



# class BlogUpdateViewBak(views.View):
#     def get(self, request, blog_id):
#         blog = get_object_or_404(Blog, id=blog_id)
#         # blog.delete()
#         # return HttpResponseRedirect(reverse('home'))
#         form = BlogForm(instance=blog)
#         context = {
#             'form': form,
#         }
#         return render(request, 'blog_create.html', context)

#     def post(self, request, blog_id):
#         blog = get_object_or_404(Blog, id=blog_id)
#         form = BlogForm(request.POST, instance=blog)
        
#         if form.is_valid():
#             print('form is valid')
#             blog = form.save()
#             return HttpResponseRedirect(reverse('blog_info', args=[blog_id]))
#         else:
#             print('form is not valid')
#             context = {
#                 'form': form,
#             }

#             return render(request, 'blog_create.html', context)


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('home')

# class BlogDeleteView(views.View):
#     def get(self, request, blog_id):
#         blog = get_object_or_404(Blog, id=blog_id)
#         blog.delete()
#         return HttpResponseRedirect(reverse('home'))


class LoginView(views.View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print('user: ', user)

        if user:
            login(request, user)

            return HttpResponseRedirect(reverse('home'))

        context = {
            'error': 'Invalid Username/Password'
        }

        return render(request, 'login.html', context)