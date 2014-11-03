import zulip
import sys
import os
import requests

class WhoIsBot(object):
    """docstring for WhoIsBot"""
    def __init__(self):
        self.email = os.environ['ZULIP_WHO_EMAIL']
        self.api_key = os.environ['ZULIP_WHO_KEY']
        self.client = zulip.Client(email, api_key)
        self.client.register(event_types=['messages'])

    def handle_messages(self, msg):
        content = msg['content'].split()
        sender_email = msg['sender_email']

        if content[0] == 'whois' or content[0] == '@**WhoIsBot**':
            name_to_lookup = content[1]
        elif 

def main():
    bot = WhoIsBot()
    bot.client.call_on_each_message(bot.handle_messages)

if __name__ == '__main__':
    main()
