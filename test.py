#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from os import getenv
from sys import exit
from notify import notify

print('---------------------------\nTWITER')
c = {
	'Consumer API Key'          : getenv('TWITTER_APIKEY', 'NOTDEF'),
	'Consumer API Security Key' : getenv('TWITTER_APISEKKEY', 'NOTDEF'),
	'Access Token'              : getenv('TWITTER_ACCSSTKN', 'NOTDEF'),
	'Accesst Security Token'    : getenv('TWITTER_ACCSSSEKTKN', 'NOTDEF')
}

a = notify('twitter', ['SystemError', 'Warning', 'Notify'])

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

a.notify('Debug', "Message A")
a.notify('Notify', "Message N")
a.notify('DBError', "Message B")

a.close()

print('---------------------------\nLOG')

c = {
	'File Name'          : 'NotifyTest.txt',
	'Append'             : True,
	'Exclusive creation' : True,
	'Flush on Notify'    : True
}

b = notify('log', ['SystemError', 'Notify'])

try:
	if b.cfg(c) == False:
		print("Twitter credentials is not valid!")
		exit(1)
except Exception as e:
	print(f"Undefined config: {e}")
	exit(1)

try:
	b.open()
except Exception as e:
	print(f"Open error/exception: {e}")
	exit(1)

b.notify('Debug', "Message A\n")
b.notify('Notify', "Message N\n")

b.close()
