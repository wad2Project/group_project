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

from stack_underflow.forms import UserProfileForm, Sign_Up_Form, CategoryForm, ReplyForm, ThreadForm
from stack_underflow.models import Category


def index(request):
    category_list = Category.objects.order_by('-threads')[:5]
    threads_list = Thread.objects.order_by('-replies')[:5]
    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['threads'] = threads_list
    return render(request, 'stack_underflow/index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        sign_Up_form = Sign_Up_Form(request.POST)
        profile_form = UserProfileForm(request.POST)

        if sign_Up_form.is_valid() and profile_form.is_valid():
            user = sign_Up_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(sign_Up_form.errors, profile_form.errors)
    else:
        sign_Up_form = Sign_Up_Form()
        profile_form = UserProfileForm()

    return render(request, 'stack_underflow/registration_form.html',
                  context = {'sign_Up_Form': sign_Up_form,
                             'profile_form': profile_form,
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

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        threads = Thread.objects.filter(category=category)
        context_dict['threads'] = threads
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['threads'] = None

    return render(request, 'stack_underflow/category.html', context=context_dict)

def show_thread(request, thread_question_slug):
    context_dict = {}

    try:
        thread = Thread.objects.get(slug=thread_question_slug)
        replies = Reply.objects.filter(thread=thread)
        context_dict['replies'] = replies
        context_dict['thread'] = thread
    except Thread.DoesNotExist:
        context_dict['replies'] = None
        context_dict['thread'] = None

    return render(request, 'stack_underflow/thread.html', context=context_dict)



@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('stack_underflow:index'))


def categories(request):
    context_dict = {}
    category_list = Category.objects.order_by('-threads')[:5]
    threads_list = Thread.objects.order_by('-replies')[:5]
    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['threads'] = threads_list


    return render(request, 'stack_underflow/categories.html', context=context_dict)



@login_required
def add_category(request):

    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()
            return redirect(reverse('stack_underflow:index'))
        else:
            print(form.errors)

    return render(request, 'stack_underflow/add_category.html', {'form' : form})

@login_required
def add_thread(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if cat is None:
        return redirect('stack_underflow:index')

    form = ThreadForm()

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            if cat:
                t = form.save(commit=False)
                t.category = cat
                t.user = request.user
                t.save()
                return redirect(reverse('stack_underflow:index'))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': cat}
    return render(request, 'stack_underflow/add_thread.html', context=context_dict)




@login_required
def add_reply(request, thread_question_slug):

    try:
        thread = Thread.objects.get(slug=thread_question_slug)
    except Thread.DoesNotExist:
        thread = None

    if thread is None:
        return redirect('stack_underflow:index')

    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST)

        if form.is_valid():
            if thread:
                reply = form.save(commit=False)
                reply.thread = thread
                reply.user = request.user
                reply.save()

                return redirect(reverse('stack_underflow:index'))

        else:
            print(form.errors)

    context_dict = {'form': form, 'thread': thread}
    return render(request, 'stack_underflow/add_reply.html', context=context_dict)

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('stack_underflow:index'))
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'stack_underflow/profile_registration.html', context_dict)
