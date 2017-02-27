from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
def index(request):
    return render(request,'blog/index.html')

#主题目录
def topics(request):
    """显示所有的主题"""
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'blog/topics.html',context)

#主题页

def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'blog/topic.html',context)
