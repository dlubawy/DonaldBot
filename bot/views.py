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

    if 'wall' in text.lower() and 'thedonald' not in sender.lower():
        donald_bot.send("I will build a great wall - and nobody builds walls better than me, believe me - and I'll build them very inexpensively. I will build a great, great wall on our southern border, and I will make %s pay for that wall. Mark my words." % sender)
    if 'birthday' in text.lower() and 'thedonald' not in sender.lower():
        donald_bot.send("An 'extremely credible source' has called my office and told me that %s's birth certificate is a fraud." % sender)
    if 'so hot' in text.lower() and 'thedonald' not in sender.lower():
        donald_bot.send("You know, it really doesn't matter what the media write as long as you've got a young, and beautiful, piece of ass.")
