from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^pizzas/$',views.pizzas,name='pizzas'),
    url(r'^pizzas/(?P<pizza_id>\d+)/$',views.pizza,name='pizza'),
]
