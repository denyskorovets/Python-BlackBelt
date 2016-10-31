from django.shortcuts import render, redirect
from .models import Users, Items
from django.contrib import messages


def index(request):
    return render(request, 'wish/index.html')


def home(request):
    return render(request, 'wish/home.html')

def registerUser(request):
    name = request.POST.get("name_up")
    username = request.POST.get("username_up")
    password = request.POST.get("pwd_up").encode()
    confirmpassword = request.POST.get("passwordconf_up").encode()
    info = Users.UserManager.register(name, username, password)
    if info[0] is True:
        request.session['name'] = username
        return redirect('/home')

    else:
        if Users.UserManager.validuser(name):
            messages.error(request, 'Enter Full Name', extra_tags='email')

        if Users.UserManager.validuser(username):
            messages.error(request, 'Username is not long enough!', extra_tags='username')

        if Users.UserManager.validemail(password):
            messages.error(request, 'Password must be at least 8 characters!', extra_tags='password')

        if Users.UserManager.matchpasswords(password, confirmpassword):
            messages.error(request, 'Password Confirmation doesn\'t match!', extra_tags='passwordconfirm')
        return redirect('/')


def loginUser(request):
    username = request.POST.get("username_in")
    password = request.POST.get('pwd_in').encode()
    Users.UserManager.login(username, password)
    if Users.UserManager.login(username, password):
        request.session['name'] = request.POST['username_in']
        return redirect('/home')
    else:
        if Users.UserManager.validuser(username):
            messages.error(request, 'Username is not long enough!!', extra_tags='username_in')
        if Users.UserManager.validpassword(password):
            messages.error(request, 'Password must be at least 8 characters!!', extra_tags='password_in')
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')