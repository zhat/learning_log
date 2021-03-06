"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^pizzas/',include('pizzas.urls',namespace='pizzas')),
    url(r'^meal_plans/',include('meal_plans.urls',namespace='meal_plans')),
    url(r'^blogs/',include('blogs.urls',namespace='blogs')),
    url(r'^users/',include('users.urls',namespace='users')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
]
