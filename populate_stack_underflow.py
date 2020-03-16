import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2project.settings')

import django
django.setup()
from stack_underflow.models import Category,Thread, Reply

def populate():

    replies = ['Example reply 1', 'Example reply 2', 'Example reply 3',
                           'Example reply 4', 'Example reply 5', 'Example reply 6',
                           'Example reply 7', 'Example reply 8', 'Example reply 9']

    programming_threads = [
        {'question': 'How to implement a linked list in Java?',
         'replies_no': 13},
        {'question': 'Should I learn C++ or C# next?',
         'replies_no': 25},
        {'question': 'What is a null pointer exception?',
         'replies_no': 53} ]

    technology_threads = [
        {'question': 'Best gaming laptop 2020?',
         'replies_no': 27},
        {'question': 'How to beat the Ender Dragon?',
         'replies_no': 1200},
        {'question': 'AI vs Machine learning?',
         'replies_no': 121 } ]

    politics_threads = [
        {'question': 'How do we elect supreme court judges in the UK?',
         'replies_no': 5},
        {'question': 'What are WTO rules?',
         'replies_no': 76},
        {'question': 'Why are some cabinet members not MPs?',
         'replies_no': 14} ]

    cats = {'Programming': {'threads': programming_threads, 'threads_no': 3600},
            'Technology': {'threads': technology_threads, 'threads_no': 2800 },
            'Politics': {'threads': politics_threads, 'threads_no': 2100 } }

    threads_list =[]

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['threads_no'])
        for t in cat_data['threads']:
            thread = add_thread(c, t['question'], t['replies_no'])
            threads_list.append(thread)

    for i in range(len(threads_list)):
        add_reply(threads_list[i], replies[i])



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
    r=Reply.objects.get_or_create(thread=thread, text=text)[0]
    r.save()
    return r


if __name__=='__main__':
    print('Starting StackUnderflow population script...')
    populate()