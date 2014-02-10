#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def send_to_twitter(msg):
    """
    Sending a message to Twitter
    """
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password('Twitter API', 'http://twitter.com/statuses', '<user_name>', '<password>')
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode({'status':msg})
    resp = urllib.request.urlopen('http://twitter.com/statuses/update.json', params)
    resp.read()