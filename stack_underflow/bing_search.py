import json
import requests
from django.db.models import Q
from django.urls import reverse

from stack_underflow.models import Category, Thread, Reply


def read_bing_key():

    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except:
        try:
            with open('../bing.key') as f:
                bing_api_key = f.readline().strip()
        except:
            raise IOError('bing.key file not found!!')
    if not bing_api_key:
        raise KeyError('Bing key not found')

    return bing_api_key


def run_query(search_terms):

    resultsCat = []
    resultsThread = []

    lookupsCat = Q(name__icontains=search_terms) | Q(threads__icontains=search_terms)
    lookupsThr = Q(question__icontains=search_terms)


    cats = Category.objects.filter(lookupsCat).distinct()
    threads = Thread.objects.filter(lookupsThr).distinct()

    for cat in cats:
        resultsCat.append({
            'title': cat.name,
            'link': reverse('stack_underflow:show_category', kwargs={'category_name_slug': cat.slug})
        })

    for thread in threads:
        resultsThread.append({
            'title': thread.question,
            'link': reverse('stack_underflow:show_thread', kwargs={'thread_question_slug': thread.slug})
        })

    bing_key = read_bing_key()
    search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_key}
    params = {'q': search_terms, 'textDecorations': True, 'textFormat': 'HTML'}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    results = []
    for result in search_results['webPages']['value']:
        results.append({
            'title': result['name'],
            'link': result['url'],
            'summary': result['snippet']})

    return results, resultsCat, resultsThread

