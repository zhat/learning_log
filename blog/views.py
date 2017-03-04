from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

#主题目录
@login_required
def topics(request):
    """显示所有的主题"""
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'blog/topics.html',context)

#主题页

@login_required
def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic=Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise Http404
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'blog/topic.html',context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method!='POST':
        #未提交数据，创建一个新表单
        form=TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('blog:topics'))

    context={'form':form}
    return render(request,'blog/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic=Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise Http404

    if request.method!='POST':
        #未提交数据，创建一个空表单
        form=EntryForm()

    else:
        #POST提交的数据，对数据进行处理
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blog:topic',args=[topic_id]))
    context={'topic':topic,'form':form}
    return render(request,'blog/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑已有的条目"""
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner!=request.user:
        raise Http404
    if request.method!='POST':
        #初次请求，使用当前条目填充表单
        form=EntryForm(instance=entry)
    else:
        #POST请求提交的数据，对数据进行处理
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topic',args=[topic.id]))
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'blog/edit_entry.html',context)

@login_required
def homepage(request):
    user=request.user
    context={}
    return render(request,'blog/homepage.html',context)
