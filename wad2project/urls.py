"""wad2project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse
from registration.backends.simple.views import RegistrationView
from stack_underflow import views

class MyRegistrationView(RegistrationView):
    def get_success_url(selfself, user):
        return reverse('stack_underflow:register_profile')

urlpatterns = [
    path('', views.index, name='index'),
    path('stack_underflow/', include('stack_underflow.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
