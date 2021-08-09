from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Mate, Comment
from .forms import mateForm, CommentForm
from django.contrib import messages
from django.db.models import Q 

# Create your views here.

def home(request):
    post = Mate.objects.all()
    postList = Mate.objects.all()
    paginator = Paginator(postList, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'home.html',{'post' : post, 'posts' : posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Mate, pk = post_id)
    comments = Comment.objects.filter(post_id=post_id, comment_id__isnull=True)

    re_comments = []
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    
    form = CommentForm()
    return render(request, 'detail.html' ,{'post' : post_detail, 'comments' : comments, 're_comments' : re_comments, 'form':form})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = mateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.writer = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('detail', post.id)
        return redirect('home')
    else:  #글을 쓰기위해 들어갔을 때
        form = mateForm()
        return render(request,'new.html', {'form':form})


def edit(request, post_id):
    post = get_object_or_404(Mate, pk = post_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = mateForm(instance = post)
        return render(request, 'edit.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = mateForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.writer = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('/checkmateapp/detail/' + str(post_id))
        return redirect('home')

def delete(request, post_id):
    post_delete =  Mate.objects.get(id = post_id)
    post_delete.delete()
    return redirect('home')

def search(request):
    keyword = request.POST.get('keyword', '')
    type = request.POST.get('type', '')
    searched_posts = Mate.objects.order_by('-id') 

    if keyword :
        if type == 'title':
            searched_posts = searched_posts.filter(title__icontains=keyword)
        elif type == 'writer':
            searched_posts = searched_posts.filter(writer__icontains=keyword)
        elif type == 'mate_type':
            searched_posts = searched_posts.filter(mate_type__icontains=keyword)    
        elif type == 'explanation':
            searched_posts = searched_posts.filter(explanation__icontains=keyword)    
        elif type == 'activity_area':
            searched_posts = searched_posts.filter(activity_area__icontains=keyword)
        return render(request, 'search.html', {'searched':keyword, 'searched_posts': searched_posts})
    else:
         return render(request, 'search.html')

def create_comment(request, article_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post_id = Mate.objects.get(pk=article_id)
            comment.author = request.user
            comment.created_at = timezone.now()
            comment.save()
    return redirect('detail', article_id)

def create_re_comment(request, article_id, comment_id):
    if request.method == 'POST':
        comment_form= CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post_id = Mate.objects.get(pk=article_id)
            comment.comment_id = Comment.objects.get(pk=comment_id)
            comment.author = request.user
            comment.created_at = timezone.now()
            comment.save()
    return redirect('detail', article_id)

def delete_comment(request, comment_id, article_id):
    mycom = Comment.objects.get(id=comment_id)
    mycom.delete()
    return redirect('detail', article_id)

