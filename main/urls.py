

from django.urls import path, include

from hardwork import settings
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', AllTaskAuthUser.as_view(), name='home'),
    path('about', about_us, name='about'),
    path('create', cache_page(60)(create_task), name='create'),
    path('register', cache_page(60)(RegisterFormViewUser.as_view()), name='register'),
    path('login', cache_page(60)(LoginUser.as_view()), name='login'),
    path('logout', logout_user, name='logout'),
    path('delete/<task_id>', delete_task, name='delete'),
    path('edit/<int:task_id>', edit_task, name='edit'),
    path('api/', include('main.api.urls'))


]
# отслеживаем по юрл и вызываем функции в файле  views

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(f'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns