import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2project.settings')

import django
django.setup()
from stack_underflow.models import Category,Thread, Reply

def populate():

    programming_threads = [
        {'question': 'How to implement a linked list in Java?',
         'replies': 13},
        {'question': 'Should I learn C++ or C# next?',
         'replies': 25},
        {'question': 'What is a null pointer exception?',
         'replies': 53} ]

    technology_threads = [
        {'question': 'Best gaming laptop 2020?',
         'replies': 27},
        {'question': 'How to beat the Ender Dragon?',
         'replies': 1200},
        {'question': 'AI vs Machine learning?',
         'replies': 121 } ]

    politics_threads = [
        {'question': 'How do we elect supreme court judges in the UK?',
         'replies': 5},
        {'question': 'What are WTO rules?',
         'replies': 76},
        {'question': 'Why are some cabinet members not MPs?',
         'replies': 14} ]

    cats = {'Programming': {'threads': programming_threads, 'threads_no': 3600},
            'Technology': {'threads': technology_threads, 'threads_no': 2800},
            'Politics': {'threads': politics_threads, 'threads_no': 2100} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['threads_no'])
        for t in cat_data['threads']:
            add_thread(c, t['question'], t['replies'])

    for c in Category.objects.all():
        for t in Thread.objects.filter(category=c):
            print(f'-{c}: {t}')

def add_thread(cat,question,replies=0):
    t = Thread.objects.get_or_create(category=cat, question=question)[0]
    t.replies = replies
    t.save()
    return t

def add_cat(name,threads=0):
    c=Category.objects.get_or_create(name=name, threads=threads)[0]
    c.save()
    return c

def add_reply(thread, text):
    r=Reply.objects.get_or_create(thread=thread, text=text)
    r.save()
    return r


if __name__=='__main__':
    print('Starting StackUnderflow population script...')
    populate()