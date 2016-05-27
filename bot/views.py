from django.shortcuts import render
import donald_tweets

def index(request):
    text = request.POST['text']
    name = '@TheDonald'
    if(name.find(text, beg=0 end=len(text)) != -1):
        donald_tweets
