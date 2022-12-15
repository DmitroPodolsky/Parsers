from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.TextField()
    time_create=models.DateTimeField(auto_now_add=True)#время публикации
    time_update = models.DateTimeField(auto_now=True)#изменение публикации
    is_published=models.BooleanField(default=True)#опубликована запись или нет
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null=True)
    user=models.ForeignKey(User,verbose_pname='Пользователь',on_delete=models.CASCADE)
    def __str__(self):
        return self.login
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Hotels(models.Model):
    name = models.TextField()
    adress = models.TextField()
    photo = models.TextField()
    description = models.TextField()
