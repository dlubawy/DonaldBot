import twitter
import os
import random
import urllib2
import json

api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'),
        consumer_secret=os.getenv('CONSUMER_SECRET'),
        access_token_key=os.getenv('ACCESS_TOKEN'),
        access_token_secret=os.getenv('ACCESS_SECRET'))

bot_id = os.getenv('BOT_ID')

def main():
    statuses = api.GetUserTimeline(screen_name='realDonaldTrump')
    rand = random.randint(0,20)
    data = {
            "bot_id" : bot_id,
            "text" : statuses[rand].text
            }
    req = urllib2.Request('https://api.groupme.com/v3/bots/post')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))

def send(message):
    data = {
            "bot_id": bot_id,
            "text": message
            }
    req = urllib2.Request('https://api.groupme.com/v3/bots/post')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
