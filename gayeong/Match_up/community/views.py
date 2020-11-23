from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import auth
from account.models import *
from .models import *
from .forms import *

# Create your views here.

def free_board(request):
    categorys = Category.objects.filter(name = "자유게시판")
    post = Community_Post.objects.filter(category__name = "자유게시판").order_by('-created_at')
    context = {
        'post':post,
        'categorys' : categorys,
    }
    return render(request, 'free_board.html', context)

def review_board(request):
    categorys = Category.objects.filter(name = "경기 후기")
    post = Community_Post.objects.filter(category__name = "경기 후기").order_by('-created_at')
    context = {
        'post':post,
        'categorys' : categorys,
    }
    return render(request, 'review_board.html', context)


def hire_board(request):
    categorys = Category.objects.filter(name = "용병 모집")
    post = Community_Post.objects.filter(category__name =  "용병 모집").order_by('-created_at')
    context = {
        'post':post,
        'categorys' : categorys,
    }
    return render(request, 'hire_board.html', context)

def createPost_free(request):
    if request.method == "POST":
        form = Community_Form(request.POST)
        print("dkdkd")
        if form.is_valid():

            username = request.user.username
            my_profile = Profile.objects.get(user__username=request.user)

            community_post = form.save(commit=False)
            community_post.author = my_profile
            cat = Category.objects.get(name = "자유게시판")
            community_post.save()
            
            community_post.category.add(cat) # 자유게시판 id값 5
            
            #author = Profile.objects.get(user__username=request.user)
            # authod_id = request.session.get('user')
            # user = Users.objects.get(pk = authod_id)
            community_post.save()

            # new_Post = Community_Post(
            #     # title = form.cleaned_data['title'],
            #     # title_image = form.cleaned_data['title_image'],
            #     # content = form.cleaned_data['content'],
            #     author = my_profile,
            #     category = get_object_or_404(Category,pk = 1),
            # )
            return redirect('/free_board')

    else:
        print("통과 불가능")
        form = Community_Form()
        context = {
            'form' : form,
        }
        return render(request, 'createPost_free.html', context)

def createPost_review(request):
    if request.method == "POST":
        form = Community_Form(request.POST)
        if form.is_valid():

            username = request.user.username
            my_profile = Profile.objects.get(user__username=request.user)

            community_post = form.save(commit=False)
            community_post.author = my_profile
            cat = Category.objects.get(name = "경기 후기")
            community_post.save()
            
            community_post.category.add(cat) # 자유게시판 id값 5
            
            #author = Profile.objects.get(user__username=request.user)
            # authod_id = request.session.get('user')
            # user = Users.objects.get(pk = authod_id)
            community_post.save()

            # new_Post = Community_Post(
            #     # title = form.cleaned_data['title'],
            #     # title_image = form.cleaned_data['title_image'],
            #     # content = form.cleaned_data['content'],
            #     author = my_profile,
            #     category = get_object_or_404(Category,pk = 1),
            # )
            return redirect('/review_board')

    else:
        form = Community_Form()
        context = {
            'form' : form,
        }
        return render(request, 'createPost_review.html', context)

def createPost_hire(request):
    if request.method == "POST":
        form = Community_Form(request.POST)
        if form.is_valid():

            username = request.user.username
            my_profile = Profile.objects.get(user__username=request.user)

            community_post = form.save(commit=False)
            community_post.author = my_profile
            cat = Category.objects.get(name = "용병 모집")
            community_post.save()
            
            community_post.category.add(cat) # 자유게시판 id값 5
            
            #author = Profile.objects.get(user__username=request.user)
            # authod_id = request.session.get('user')
            # user = Users.objects.get(pk = authod_id)
            community_post.save()

            # new_Post = Community_Post(
            #     # title = form.cleaned_data['title'],
            #     # title_image = form.cleaned_data['title_image'],
            #     # content = form.cleaned_data['content'],
            #     author = my_profile,
            #     category = get_object_or_404(Category,pk = 1),
            # )
            return redirect('/hire_board')

    else:
        form = Community_Form()
        context = {
            'form' : form,
        }
        return render(request, 'createPost_hire.html', context)

def turnBack(request, id):
    post = Community_Post.objects.filter(pk = id)
    cat = post.category.name
    print(post.category)
    if(cat == "자유게시판"):
        return redirect('/free_board')

    elif(cat == "경기 후기"):
        return redirect('/review_board')

    elif(cat == "용병 모집"):
        return redirect('/hire_board')

    else:
        return redirect('account:main')

    
def postDetail(request, id):
    post = get_object_or_404(Community_Post, pk = id)
    context = {
        'post' : post,
    }
    return render(request, 'postDetail.html', context)

def postDelete(request, id):
    post = get_object_or_404(Community_Post, pk=id)
    post.delete()
    return redirect("/free_board")

def postEdit(request, id):
    post = get_object_or_404(Community_Post, pk = id)
    context = {
        'post': post,
        'dform' : Community_Form(instance = Community_Post),
    }

    return render(request, 'postEdit.html', context)

def postUpdate(request, id):
    post = get_object_or_404(Community_Post, pk = id)
    dform = Community_Form(request.POST, instance = Community_Post)
    if dform.is_valid():
        dform.save()
    return redirect('/postDtail/'+id)