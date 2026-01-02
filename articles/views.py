from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment
from django.db.models import Q

def posts_by_category(request, category_id):
    posts = Article.objects.filter(status=1, category_id=category_id)
    #category = get_object_or_404(Category, pk=category_id)

    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')

    return render(request, 'posts-by-category.html', { 'posts': posts, 'category': category })

def articles(request, slug):
    article = get_object_or_404(Article, status=1, slug=slug)

    if request.method == 'POST':
        comment = Comment()

        comment.user = request.user
        comment.article = article
        comment.text = request.POST['comment']

        comment.save()

        return redirect(request.path_info)

    comments = Comment.objects.filter(article=article)

    return render(request, 'articles.html', { 'article': article, 'comments': comments })

def search(request):
    keyword = request.GET.get('keyword')

    posts = Article.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(body__icontains=keyword), status=1)

    return render(request, 'search.html', { 'posts': posts, 'keyword': keyword })
