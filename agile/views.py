from django.shortcuts import render, redirect

from django.views.generic import DetailView

from .models import Agile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts/login/')
def homepage(request):
    return render(request, 'index.html', {'name': 'Agile Story'})


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


def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(username, email, password)
    if user:
        return redirect('/agile/homepage', locals())
    else:
        return redirect('/signup', locals())

@login_required(login_url='accounts/login/')
def article_index(request):
    name = 'Archive'
    Articles = Agile.objects.all()
    return render(request, 'index.html', locals())


def singleAgile(request, pk):
    agile_list = Agile.objects.get(title=pk)
    context = {
        'agile_list': agile_list
    }
    return render(request, 'detail.html', context)


class AgileDetail(DetailView):
    model = Agile
    template_name = 'detail.html'

