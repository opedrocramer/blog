from django.shortcuts import render, redirect, get_object_or_404
from articles.models import Category, Article
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ArticleForm, AddUserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    posts_count = Article.objects.all().count()

    return render(request, 'dashboard/dashboard.html', { 'category_count': category_count, 'posts_count': posts_count })

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request, 'dashboard/add-category.html', { 'form': form })

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'dashboard/edit-category.html', { 'form': form, 'category': category })

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    category.delete()

    return redirect('categories')

def posts(request):
    posts = Article.objects.all()

    return render(request, 'dashboard/posts.html', { 'posts': posts })

def add_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)

            post.author = request.user
            post.save()

            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)

            post.save()

            return redirect('posts')
    else:
        form = ArticleForm()

    return render(request, 'dashboard/add-post.html', { 'form': form })

def edit_post(request, pk):
    post = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)
            post.save()

            return redirect('posts')
    else:
        form = ArticleForm(instance=post)

    return render(request, 'dashboard/edit-post.html', { 'form': form, 'post': post })

def delete_post(request, pk):
    post = get_object_or_404(Article, pk=pk)

    post.delete()

    return redirect('posts')

def users(request):
    users = User.objects.all()

    return render(request, 'dashboard/users.html', { 'users': users })

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('users')
    else:
        form = AddUserForm()

    return render(request, 'dashboard/add-user.html', { 'form': form })

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()

            return redirect('users')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'dashboard/edit-user.html', { 'form': form })

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    user.delete()

    return redirect('users')
