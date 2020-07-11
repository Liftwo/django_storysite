if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user and user.is_staff is False:
        auth.login(request, user)
        return redirect('/agile/')
    elif user and user.is_staff is True:
        auth.login(request, user)
        return redirect('/agile/')
    else:
        return redirect('/agile/')
else:
    return render(request, 'login_custom.html', locals())

def singleAgile(request, pk):
    agile_list = Agile.objects.get(title=pk)

    context = {
    'agile_list': agile_list
    }
    return render(request, 'detail.html', context)

def post_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/agile/login_custom/', locals())
    else:
        return redirect('/agile/', locals())

def singleAgile(request, index):
    index = get_object_or_404(Agile, index=index)
    # title = get_object_or_404(Agile, title=title)
    return render(request, 'detail.html', {'index':index})