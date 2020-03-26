from django import forms
from django.contrib.auth.models import User
from stack_underflow.models import UserProfile, Category, Thread, Reply

class Sign_Up_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class ThreadForm(forms.ModelForm):

    question = forms.CharField(max_length=128,
                               help_text="Please enter a question")
    replies = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Thread
        fields = ('question',)

class ReplyForm(forms.ModelForm):
    text = forms.CharField(max_length=2000,
                           help_text='Please enter a reply')


    class Meta:
        model = Reply
        fields = ('text',)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)



