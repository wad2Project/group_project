from django.contrib import admin
from stack_underflow.models import Category, Thread, Reply, UserProfile, Notification

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Reply)
admin.site.register(UserProfile)
admin.site.register(Notification)


