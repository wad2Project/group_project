from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context_dict = {'boldmessage': 'Hello'}
    return render(request, 'stack_underflow/index.html', context=context_dict)
