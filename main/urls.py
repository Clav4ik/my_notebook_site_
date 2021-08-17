

from django.urls import path, include

from hardwork import settings
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', MainView.as_view(), name='home'),
    path('about', cache_page(60)(about), name='about'),
    path('create', cache_page(60)(create), name='create'),
    path('trueregister', cache_page(60)(RegisterFormView.as_view()), name='trueregister'),
    path('login', cache_page(60)(LoginUser.as_view()), name='login'),
    path('logout', logout_user, name='logout'),
    path('delete/<task_id>', delete_task, name='delete'),
    path('edit/<int:task_id>', edit, name='edit'),
    path('api/', include('main.api.urls'))


]
# отслеживаем по юрл и вызываем функции в файле  views

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(f'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns