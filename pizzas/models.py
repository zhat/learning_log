from django.db import models

# Create your models here.
class Pizza(models.Model):
    name=models.CharField('披萨名称',max_length=50)

    class Meta:
        verbose_name='披萨'
        verbose_name_plural='披萨'
    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza=models.ForeignKey(Pizza,verbose_name='披萨')
    name=models.CharField('配料',max_length=50)

    class Meta:
        verbose_name='配料'
        verbose_name_plural='配料'

    def __str__(self):
        return self.name

