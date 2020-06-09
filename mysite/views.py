from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


# def here(request):
#     return HttpResponse('Hell, let get it')


def index(request):
    return render(request, 'index.html', {'name': 'Agile Story'})

def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(username, email, password)
    if user:
        return redirect('/', locals())
    else:
        return redirect('/signup', locals())