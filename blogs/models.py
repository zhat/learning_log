from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField('标题',max_length=50)
    text=models.TextField('博客内容')
    date_added=models.DateTimeField('添加时间',auto_now_add=True)
    class Meta:
        verbose_name="博客"
        verbose_name_plural="博客"
    def __str__(self):
        return self.title
