from django.shortcuts import render, redirect
from .models import vlog, Category
from django.contrib.auth import authenticate, login
from .forms import VlogForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm


def vlog_list(request):
    blogs=vlog.objects.all()
    categories=Category.objects.all()
    context={
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'vlog/blog_list.html', context)


def vlog_detail(request, pk):
    blog=vlog.objects.get(id=pk)
    context={
        'blog': blog,
    }
    return render(request, 'vlog/vlog_detail.html', context)


def category_filter(request, pk):

    blogs=vlog.objects.filter(category=pk)
    categories=Category.objects.all()
    context={
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'vlog/category.html', context)


def signup(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vlog_list')
    else:
        form=SignUpForm()
    return render(request, 'registration/signup.html', {'form', form})


def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd['username']
            password=cd['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vlog_list')
    else:
        form=AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def create(request):
    if request.method=='POST':
        form=VlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vlog_list')
    else:
        form=VlogForm()
    context={
        'form': form,
    }
    return render(request, 'vlog/create.html', context)


def update(request, pk):
    blog=vlog.objects.get(id=pk)
    if request.method=='POST':
        form=VlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vlog_list')
    else:
        form=VlogForm()
    context={
        'form': form,
    } 
    return render(request, 'vlog/update.html', context)


def delete(request, pk):
    blog=vlog.objects.get(id=pk)
    if request.method=="POST":
        blog.delete()
        return redirect('vlog_list')
    context={
        'blog': blog,
    }
    return render(request, 'vlog/delete.html', context)
