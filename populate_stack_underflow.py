import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2project.settings')

import django
django.setup()
from stack_underflow.models import Category,Thread, Reply
from django.contrib.auth.models import User
from django.db import IntegrityError

def populate():
    user = User.objects.create_user('username', 'user@gmail.com', 'password1234')
    replies = [
        {'reply': 'Example reply 1?', 'user': user},
        {'reply': 'Example reply 2?', 'user': user},
        {'reply': 'Example reply 3?', 'user': user},
        {'reply': 'Example reply 4?', 'user': user},
        {'reply': 'Example reply 5?', 'user': user},
        {'reply': 'Example reply 6?', 'user': user},
        {'reply': 'Example reply 7?', 'user': user},
        {'reply': 'Example reply 8?', 'user': user},
        {'reply': 'Example reply 9?', 'user': user} ]


    programming_threads = [
        {'question': 'How to implement a linked list in Java?',
         'replies_no': 13, 'user': user},
        {'question': 'Should I learn C++ or C# next?',
         'replies_no': 25, 'user': user},
        {'question': 'What is a null pointer exception?',
         'replies_no': 53, 'user': user} ]

    technology_threads = [
        {'question': 'Best gaming laptop 2020?',
         'replies_no': 27, 'user': user},
        {'question': 'How to beat the Ender Dragon?',
         'replies_no': 1200, 'user': user},
        {'question': 'AI vs Machine learning?',
         'replies_no': 121, 'user': user} ]

    politics_threads = [
        {'question': 'How do we elect supreme court judges in the UK?',
         'replies_no': 5, 'user': user},
        {'question': 'What are WTO rules?',
         'replies_no': 76, 'user': user},
        {'question': 'Why are some cabinet members not MPs?',
         'replies_no': 14, 'user': user} ]

    cats = {'Programming': {'threads': programming_threads, 'threads_no': 3600, 'user': user},
            'Technology': {'threads': technology_threads, 'threads_no': 2800, 'user': user},
            'Politics': {'threads': politics_threads, 'threads_no': 2100, 'user': user} }

    threads_list =[]

    for cat, cat_data in cats.items():
        c = add_cat(cat_data['user'], cat, cat_data['threads_no'])
        for t in cat_data['threads']:
            thread = add_thread(t['user'], c, t['question'], t['replies_no'])
            threads_list.append(thread)

    for i in range(len(threads_list)):
        add_reply(replies[i]['user'], threads_list[i], replies[i]['reply'])


    for c in Category.objects.all():
        for t in Thread.objects.filter(category=c):
            print(f'-{c}: {t}')


def add_thread(user, cat,question,replies=0):
    t = Thread.objects.get_or_create(category=cat, question=question, user=user)[0]
    t.replies = replies
    t.save()
    return t

def add_cat(user, name,threads=0):
    c=Category.objects.get_or_create(name=name, threads=threads, user=user)[0]
    c.save()
    return c

def add_reply(user, thread, text):
    r=Reply.objects.get_or_create(thread=thread, text=text, user=user)[0]
    r.save()
    return r


if __name__=='__main__':
    print('Starting StackUnderflow population script...')
    populate()