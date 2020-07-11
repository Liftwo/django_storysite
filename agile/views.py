from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import DetailView

from .models import Agile, Register, Visit
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import RegisterForm


def homepage(request):
    visit_model = Visit.objects.get(pk=1)
    visit_model.times+=1
    visit_model.save()
    context = {'name': 'Agile Story', 'visit_template': visit_model.times}
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/agile')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'register.html', context)


def get_signup(request):
    return render(request, 'signup.html')


def post_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_staff is False:
            auth.login(request, user)
            return redirect('/agile/')
        elif user and user.is_staff is True:
            auth.login(request, user)
            return redirect('/agile/show_register')
        else:
            return redirect('/agile/')
    else:
        return render(request, 'registration/login_custom.html', locals())


def post_logout(request):
    auth.logout(request)
    return redirect('/agile/')


@login_required(login_url='/agile/login_custom')
def article_index(request):
    name = 'Archive'
    Articles = Agile.objects.all()
    return render(request, 'index.html', locals())


@login_required(login_url='/agile/login_custom')
def singleAgile(request, pk):
    agile_list = Agile.objects.get(index=pk)

    context = {
    'agile_list': agile_list
    }
    return render(request, 'detail.html', context)


class AgileDetail(DetailView):
    model = Agile
    template_name = 'detail.html'


def register_create_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        Register.objects.create(**form.cleaned_data)
        form = RegisterForm
    context = {
        'form':form
    }
    return render(request, 'register_create.html', context)


@user_passes_test(lambda user:user.is_staff, login_url='/agile/')
def show_register(request):
    register_list = Register.objects.all()
    context = {'register_list':register_list}
    return render(request, 'show_register.html', context)


def test(request):
    return render(request, 'test.html')


