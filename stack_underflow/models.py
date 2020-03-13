from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class User(models.Model):
    #Anything else needed here?
    loggedIn = models.BooleanField()#default=false?

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.userName

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    threads = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Thread(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    replies = models.IntegerField(default=0)



    def __str__(self):
        return self.question

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)

class Notification(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)












