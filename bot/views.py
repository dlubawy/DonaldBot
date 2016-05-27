from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import imp
donald_bot = imp.load_source('donald_bot', 'bot/donald_bot.py')

@csrf_exempt
def index(request):
    json_data = json.loads(request.body)

    text = json_data['text']
    sender = json_data['name']
    
    name = '@thedonald'
    
    if name in text.lower():
        donald_bot.tweet()
    if 'wall' in text.lower():
        donald_bot.send("I'll build it higher, and make %s pay for it." % sender)
