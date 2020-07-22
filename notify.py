#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import tweepy

notifyTypes = ['log', 'twitter', 'discord', 'telegram']
notifyLevels = ['MustNotify', 'SystemError', 'DBError', 'Warning', 'Notify', 'Debug']

# Factory pattern in Python is the eighth egyptian plague. Is the most stupid thing:
# https://realpython.com/factory-method-python/

class notifyLog():
	def __init__(self):
		print('log __init__')

	def cfg(self):
		print('log cfg')

	def open(self):
		print('log open')

	def notify(selfself, msg):
		print('log notify')

	def close(self):
		print('log close')

class notifyTwitter():
	ConsAPIKey    = str()
	ConsAPIKeySek = str()
	AccssTkn      = str()
	AccssTknSek   = str()
	twttcli       = object()
	twttAuth      = object()
	lastStatus    = object()
	usrTwtt       = object()

	def __init__(self):
		self.ConsAPIKey    = str()
		self.ConsAPIKeySek = str()
		self.AccssTkn      = str()
		self.AccssTknSek   = str()
		self.twttcli       = object()
		self.twttAuth      = object()
		self.lastStatus    = object()
		self.usrTwtt       = object()
		print('twitter __init__')

	def cfg(self, consapikey : str, consapikeysek : str, accsstkn : str, accsstknsek : str) -> bool:
		self.ConsAPIKey    = consapikey
		self.ConsAPIKeySek = consapikeysek
		self.AccssTkn      = accsstkn
		self.AccssTknSek   = accsstknsek

		self.twttAuth = tweepy.OAuthHandler(self.ConsAPIKey, self.ConsAPIKeySek)
		self.twttAuth.set_access_token(self.AccssTkn, self.AccssTknSek)

		self.twttcli = tweepy.API(self.twttAuth)

		print('twitter cfg')

		try:
			self.usrTwtt = self.twttcli.verify_credentials()
			return True
		except:
			return False

	def open(self):
		print('twitter open')

	def notify(selfself, msg):
		print('twitter notify')
		self.lastStatus = self.twttcli.update_status(message)
		return self.lastStatus

	def close(self):
		print('twitter close')

class notify(Exception):
	_type = str('')
	_notifyObj = object()
	_level = list('')

	def __init__(self, t : str = '', l : list = []):

#		if self.__class__ == notify:
#			raise NotImplementedError("Interfaces can't be instantiated")

		if t not in notifyTypes:
			raise TypeError(f"Notify must be one of: {notifyTypes}")

		if t == notifyTypes[0]:
			self._type = t
			self._notifyObj = notifyLog()

		if t == notifyTypes[1]:
			self._type = t
			self._notifyObj = notifyTwitter()

		if t == notifyTypes[2]:
			self._type = t
			self._notifyObj = None

		if t == notifyTypes[3]:
			self._type = t
			self._notifyObj = None

		self._level = list(set(l) & set(notifyLevels))

	def cfg(self):
		return self._notifyObj.close()

	def open(self):
		return self._notifyObj.open()

	def notify(self, level, msg):
		return self._notifyObj.notify(msg)

	def close(self):
		return self._notifyObj.close()

	def levelAdd(self, l : list = ''):
		self._level = self._level + list(set(l) & set(notifyLevels))
		print(self._level)

	def levelRemove(self, l : str = ''):
		self._level.remove(l)

	def level(self) -> list:
		return self._level
