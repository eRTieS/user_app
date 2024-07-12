from django.shortcuts import render, redirect
from django.http import HttpResponse

from user_manager.models import User
from user_manager.forms import NewUserForm


def index(request):
    new_user_form = NewUserForm()
    return render(request, 'index.html', {'new_user_form': new_user_form})


def list_users(request):
    users = User.objects.all()

    return render(request, 'users.html', {"users": users})


def add_user(request):
    user = User(
        name=request.POST['name'],
        email=request.POST['email'],
        phone=request.POST['phone']
    )
    user.save()
    return redirect('/')


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

    users = User.objects.all()

    return render(request, 'users.html', {"users": users})


def update_user(request, user_id):
    user = User.objects.get(id=user_id)

    user.name = request.POST['name']
    user.email = request.POST['email']
    user.phone = request.POST['phone']
    user.save()

    users = User.objects.all()

    return render(request, 'users.html', {"users": users})
