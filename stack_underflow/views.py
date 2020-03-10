from django.shortcuts import render
from django.http import HttpResponse
from stack_underflow.forms import Sign_Up_Form


def index(request):

    context_dict = {'boldmessage': 'Hello'}
    return render(request, 'stack_underflow/index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        sign_Up_form = Sign_Up_Form(request.POST)

        if sign_Up_Form.is_valid():
            user = sign_Up_Form.save()

            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(sign_Up_Form.errors)
    else:
        sign_Up_Form = Sign_Up_Form()

    return render(request, 'stack_underflow/register.html',
                  context = {'sign_Up_Form': sign_Up_Form,
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
