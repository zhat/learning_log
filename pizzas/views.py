from django.shortcuts import render
from .models import Pizza,Topping
# Create your views here.
def index(request):
    return render(request,'pizzas/index.html')
#披萨列表页
def pizzas(request):
    """显示所有披萨"""
    pizzas=Pizza.objects.order_by('id')
    context={'pizzas':pizzas}
    return render(request,'pizzas/pizzas.html',context)

#披萨详情页
def pizza(request,pizza_id):
    """显示单个披萨及其所有的配料"""
    pizza=Pizza.objects.get(id=pizza_id)
    toppings=pizza.topping_set.order_by('id')
    context={'pizza':pizza,'toppings':toppings}
    return render(request,'pizzas/pizza.html',context)
