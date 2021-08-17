from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, authenticate
from django.http import  HttpResponseNotFound
from django.core.paginator import Paginator

from .models import Task
from .forms import TaskForm
from .forms import RegisterUserForm
from .forms import LoginUserForm


def about(request):

    return render(request, "main/about.html")


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            tasks = form.save(commit=False)
            tasks.created_by = request.user
            form.save()
            return redirect('home')  # переадресация на страничку home
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error

    }
    return render(request, "main/create.html", context)


class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request):
        if request.user.is_authenticated:

            task = Task.objects.filter(created_by=request.user).order_by('-id')
            paginator = Paginator(task, 5)

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                                       'tasks': task,
                                                       'page_obj': page_obj})
        else:

            form = TaskForm()

        return render(request, 'main/index.html', {'title': 'Главная страница сайта','form': form})


class RegisterFormView(CreateView):
    form_class = RegisterUserForm
    success_url = "login"
    template_name = 'main/trueregister.html'


    def form_valid(self, form):

        form.save()

        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        LoginUserForm(self.request, user)
        return super(RegisterFormView, self).form_valid(form)

    class Meta:
        model = User
        fields = ['username', 'password',  'password2', 'captcha']




class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy("home")


# or in settings.py as LOGIN_REDIRECT_URL = ''


def logout_user(request):
    logout(request)
    return redirect('login')


def delete_task(request, task_id):
    post_to_delete = get_object_or_404(Task, pk=task_id)
    post_to_delete.delete()
    return redirect('home')


def edit(request, task_id):
    post_to_edit = get_object_or_404(Task, pk=task_id, created_by=request.user)

    try:
        if request.method == "POST":
            post_to_edit.title = request.POST.get("title")
            post_to_edit.task = request.POST.get("task")
            post_to_edit.save()
            return redirect('home')
        else:
            context = {}
            context['form'] = TaskForm(instance=post_to_edit)
            return render(request, "main/edit.html", {'title':'Редактирование', 'tasks': context})
    except post_to_edit.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
