

from django.db import models, IntegrityError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', primary_key=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True, default='logo2.png')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    threads = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=128, unique=True)
    replies = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    #url = models.URLField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.question

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'

    def save(self, *args, **kwargs):
        super(Reply, self).save(*args, **kwargs)

    def __str__(self):
        return self.text











