from audioop import reverse
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset


class Client(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.PROTECT, null=True)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)

    def __str__(self):
        return 'Имя - {0}, Фамилия - {1}'.format(self.name, self.surname)
