from django.contrib import admin
from .models import  Task
from .models import  Client
# Register your models here.

admin.site.register(Task)
admin.site.register(Client)
admin.site.site_header = 'Админ-панель'
