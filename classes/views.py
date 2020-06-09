from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from classes.models import Photo
from django.contrib.auth.models import User


def index(request):
    return render(request, 'template_whoami.html', {'now':str(datetime.today()),
    })





def get_signup(request):
    return render(request, 'signup.html')


def photo_index(request):
    name = 'Photo House'
    Photos = Photo.objects.all()
    return render(request, 'index.html', locals())


def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(username, email, password)
    if user:
        return redirect('/classes/test', locals())
    else:
        return redirect('/signup', locals())


from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/classes/test')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'register.html', context)

