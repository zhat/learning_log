from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^blogs/$',views.blogs,name='blogs'),
    url(r'^blog/(?P<blog_id>\d+)$',views.blog,name='blog'),
    url(r'^add_blog/$',views.add_blog,name='add_blog'),
    url(r'^edit_blog/(?P<blog_id>\d+)$',views.edit_blog,name='edit_blog'),
    url(r'^login/$',login,{'template_name':'blogs/login.html'},name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^register/$',views.register,name='register'),
]
