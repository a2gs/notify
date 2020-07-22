#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from os import getenv
from sys import exit
import notify

c = {
	'Consumer API Key'          : getenv('TWITTER_APIKEY', 'NOTDEF'),
	'Consumer API Security Key' : getenv('TWITTER_APISEKKEY', 'NOTDEF'),
	'Access Token'              : getenv('TWITTER_ACCSSTKN', 'NOTDEF'),
	'Accesst Security Token'    : getenv('TWITTER_ACCSSSEKTKN', 'NOTDEF')
}

a = notify.notify('twitter', ['SystemError', 'Warning', 'Notify'])

try:
	if a.cfg(c) == False:
		print("Twitter credentials is not valid!")
		exit(1)
except Exception as e:
	print(f"Undefined config: {e}")
	exit(1)

a.levelAdd(['Debug'])

try:
	a.open()
except Exception as e:
	print(f"Open error/exception: {e}")
	exit(1)


a.notify('Debug', "Message Aaa")
a.notify('Notify', "Message Nnn")
a.notify('DBError', "Message Bbb")

print("Ok")
