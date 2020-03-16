from django import forms
from django.contrib.auth.models import User
from stack_underflow.models import UserProfile, Category, Thread

class Sign_Up_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name")

    class Meta:
        model = Category
        fields = ('name',)

class ThreadForm(forms.ModelForm):
    category = forms.CharField(max_length=128,
                               help_text="Please enter the category you wish to add a thread to")
    question = forms.CharField(max_length=128,
                               help_text="Please enter a question")
    replies = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Thread
        fields = ('category', 'question')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data


