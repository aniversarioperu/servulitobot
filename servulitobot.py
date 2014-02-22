#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plivo
import config
import argparse
import sys
from argparse import RawTextHelpFormatter
import urllib
import api
import requests

def is_server_up(website):
    # Check if server is up and running
    try:
        http_code = urllib.urlopen(website).getcode()
        if http_code == 200:
            return True
    except:
        return False


def tell_using_twitter(message, twitter_user):
    oauth = api.get_oauth()

    # send a @mention
    status = "@" + twitter_user + " " + message
    payload = {
            'status': status,
            }
    url = "https://api.twitter.com/1.1/statuses/update.json"
    try:
        r = requests.post(url=url, auth=oauth, params=payload)
    except:
        print "Error", r.text

    # send a DM
    payload = {
            'text': message,
            'screen_name': twitter_user,
            }
    url = "https://api.twitter.com/1.1/direct_messages/new.json"
    try:
        r = requests.post(url=url, auth=oauth, params=payload)
        if 'errors' in r.text:
            print r.text['errors']['message']
    except:
        print "Error", r.text



def send_sms(message, destination):
    # Your PLIVO_AUTH_ID and PLIVO_AUTH_TOKEN can be found on your Plivo Dashboard
    # https://manage.plivo.com/dashboard
    PLIVO_AUTH_ID = config.auth_id
    PLIVO_AUTH_TOKEN = config.auth_token

    # Enter your Plivo phone number. This will show up on your caller ID
    plivo_number = "00018324723345"

    # Enter the phone number that you would like to receive your SMS
    destination_number = destination


    # Enter the SMS that you want to send
    text = message

    message_params = {
        'src':plivo_number,
        'dst':destination_number,
        'text':text,
        }

    p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

    print p.send_message(message_params)

def main():
    description = """Findout if the server hosting your website is down. If
    positive, then @ServulitoBot will let you know via Twitter by DM and
    @mention.
    This bot will also send you a SMS to your mobile phone. So that
    you can move your ass and turn on the sever."""

    parser = argparse.ArgumentParser(description=description,formatter_class=RawTextHelpFormatter)
    parser.add_argument('-w', '--website', action='store',
            metavar='http://utero.pe',
            help='Your website URL address to check if it is up and running',
            required=True, dest='website')
    parser.add_argument('-m', '--message', action='store',
            metavar='\'Hola que hace?\'',
            help='The message you want to text using SMS and Twitter',
            required=True, dest='message')
    parser.add_argument('-d', '--destination', action='store',
            metavar='+51900755700',
            help='Destination mobile phone number',
            required=False, dest='destination')
    parser.add_argument('-t', '--twitter_user', action='store',
            metavar='uterope',
            help='Twitter username (twitter handle)',
            required=True, dest='twitter_user')

    args = parser.parse_args()

    website = args.website.strip()
    message = args.message.strip()
    twitter_user = args.twitter_user.strip()

    if args.destination:
        destination = args.destination.strip()

    server_up = is_server_up(website)

    if server_up == False:
        # our server is down. Call the guys
        if destination:
            send_sms(message, destination)
        tell_using_twitter(message, twitter_user)


if __name__ == "__main__":
    main()
