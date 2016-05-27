from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json, imp, random
donald_bot = imp.load_source('donald_bot', 'bot/donald_bot.py')

@csrf_exempt
def index(request):
    json_data = json.loads(request.body)

    text = json_data['text']
    sender = json_data['name']
    
    name = '@thedonald'
    command = '@thedonald how'

    if command in text.lower():
        s = text.split()
        minus_punct = s[4][:len(s[4])-1]
        rand = random.randint(0,100)
        if '?' in s[4]:
            donald_bot.send("{0} is {1}% {2}".format(minus_punct, rand, s[2]))
        else:
            donald_bot.send("{0} is {1}% {2}".format(s[4], rand, s[2]))
    elif name in text.lower():
        donald_bot.tweet()

    if 'wall' in text.lower():
        donald_bot.send("I'll build the wall higher and make %s pay for it." % sender)
