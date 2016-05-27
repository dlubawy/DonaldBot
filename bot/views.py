from django.shortcuts import render
import imp
donald_tweets = imp.load_source('donald_tweets', 'bot/donald_tweets.py')

def index(request):
    text = request.POST['text']
    name = '@TheDonald'
    if(name.find(text, beg=0, end=len(text)) != -1):
        main()
