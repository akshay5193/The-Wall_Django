from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.


def index(request):
    return render(request, "login_reg/index.html")


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')

    else:
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
        request.session['user_id'] = new_user.id
        context = {
            'user_first_name': new_user.first_name,
            'user_last_name': new_user.last_name
        }
        print("user registered successfully")
        return redirect("/wall")
        # return render(request, "the_wall/wall_index.html", context)


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        matching_users = User.objects.filter(email=request.POST['email'])
        if matching_users:
            current_user = matching_users[0]

            if bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode()):
                request.session['user_id'] = current_user.id
                print(
                    "Got the user right and now going to its wall!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return redirect('/wall')
            else:
                messages.error(
                    request, "Incorrect Password, please try again!")
                return redirect('/')


# def home(request):
#     if request.session.get('user_id'):
#         current_user = User.objects.get(id=request.session.get('user_id'))
#         context = {
#             'first_name': current_user.first_name
#         }
#         return render(request, "the_wall/wall_index.html", context)
#     return redirect('/')
