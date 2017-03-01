from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.
def index(request):
    return render(request,'blogs/index.html')
def blogs(request):
    blogs=BlogPost.objects.all()
    context={'blogs':blogs}
    return render(request,'blogs/blogs.html',context)


def blog(request,blog_id):
    """显示单个主题及其所有的条目"""
    blog=BlogPost.objects.get(id=blog_id)
    context={'blog':blog}
    return render(request,'blogs/blog.html',context)

def add_blog(request):
    """添加新主题"""
    if request.method!='POST':
        #未提交数据，创建一个新表单
        form=BlogPostForm()
    else:
        #POST提交的数据，对数据进行处理
        form=BlogPostForm(request.POST)
        if form.is_valid():
            blog=form.save()
            return HttpResponseRedirect(reverse('blogs:blog',args=[blog.id]))

    context={'form':form}
    return render(request,'blogs/add_blog.html',context)

def edit_blog(request,blog_id):
    """编辑已有的条目"""
    blog=BlogPost.objects.get(id=blog_id)
    if request.method!='POST':
        #初次请求，使用当前条目填充表单
        form=BlogPostForm(instance=blog)
    else:
        #POST请求提交的数据，对数据进行处理
        form=BlogPostForm(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blog',args=[blog.id]))
    context={'blog':blog,'form':form}
    return render(request,'blogs/edit_blog.html',context)

#注销
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

#注册
def register(request):
    """注册新用户"""
    if request.method!='POST':
        #显示空的注册表单
        form=UserCreationForm()
    else:
        #处理填好的表单
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            #让用户自动登录，再重定向到主页
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))
    context={'form':form}
    return render(request,'blogs/register.html',context)
