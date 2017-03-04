from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text=models.CharField('主题名称',max_length=200)
    date_added=models.DateTimeField('添加时间',auto_now_add=True)
    owner=models.ForeignKey(User)

    class Meta:
        verbose_name="主题"
        verbose_name_plural="主题"
    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic=models.ForeignKey(Topic,verbose_name='主题')
    text=RichTextField('内容')
    date_added=models.DateTimeField('添加时间',auto_now_add=True)

    class Meta:
        verbose_name='主题内容'
        verbose_name_plural='主题内容'

    def __str__(self):
        '''返回模型的字符串表示'''
        if len(self.text)<50:
            return self.text
        return self.text[:50]+"..."

