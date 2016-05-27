from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import imp
donald_tweets = imp.load_source('donald_tweets', 'bot/donald_tweets.py')

@csrf_exempt
def index(request):
    json_data = json.loads(request.body)
    text = json_data['text']
    name = '@TheDonald'
    if name in text:
        donald_tweets.main()
