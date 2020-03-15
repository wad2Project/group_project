from django.shortcuts import render
from django.http import HttpResponse
from stack_underflow.models import Category
from stack_underflow.models import Thread
from stack_underflow.models import Reply
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

from stack_underflow.forms import Sign_Up_Form
from stack_underflow.models import Category


def index(request):
    category_list = Category.objects.order_by('-threads')[:5]
    context_dict = {}
    context_dict['categories'] = category_list
    return render(request, 'stack_underflow/index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        sign_Up_form = Sign_Up_Form(request.POST)

        if sign_Up_form.is_valid():
            user = sign_Up_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(sign_Up_form.errors)
    else:
        sign_Up_form = Sign_Up_Form()

    return render(request, 'stack_underflow/register.html',
                  context = {'sign_Up_Form': sign_Up_form,
                             'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('stack_underflow:index'))
            else:
                return HttpResponse("Your StackUnderflow account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'stack_underflow/login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('stack_underflow:index'))


def categories(request):
    context_dict = {}
    return render(request, 'stack_underflow/categories.html', context=context_dict)

<<<<<<< HEAD

def add_category(request):
    return render(request, 'stack_underflow/add_category.html')

#PARTIAL ADD_REPLY- NOT FINISHED
def add_reply(request,thread_name):

    try:
        thread = Thread.objects.get(thread_name)
    except Thread.DoesNotExist:
        thread = None

    if thread is None:
        return redirect('/stack_underflow/')

    #does not exist yet
    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST)

        if form.is_Valid():
            if thread:
                reply = form.save(commit=False)
                reply.thread = thread
                reply.save()

                return redirect(reverse(''))

        else:
            print(form.errors)

        context_dict = {'form' : form, 'thread' : thread}
        return render(request, 'stack_underflow/add_reply.html', context=context_dict)
