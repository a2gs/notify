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

	def cfg(self, c : dict = {}):
		print('log cfg')

	def open(self):
		print('log open')

	def notify(selfself, msg):
		print('log notify')

	def close(self):
		print('log close')

class notifyTwitter():
	_ConsAPIKey    = str()
	_ConsAPIKeySek = str()
	_AccssTkn      = str()
	_AccssTknSek   = str()
	_twttcli       = object()
	_twttAuth      = object()
	_lastStatus    = object()
	_usrTwtt       = object()

	def __init__(self):
		self._ConsAPIKey    = str()
		self._ConsAPIKeySek = str()
		self._AccssTkn      = str()
		self._AccssTknSek   = str()
		self._twttcli       = object()
		self._twttAuth      = object()
		self._lastStatus    = object()
		self._usrTwtt       = object()

	def cfg(self, c : dict = {}):
		try:
			self._ConsAPIKey    = c['Consumer API Key']
			self._ConsAPIKeySek = c['Consumer API Security Key']
			self._AccssTkn      = c['Access Token']
			self._AccssTknSek   = c['Accesst Security Token']
		except Exception as e:
			raise (e)

	def open(self) -> bool:
		try:
			self._twttAuth = tweepy.OAuthHandler(self._ConsAPIKey, self._ConsAPIKeySek)
			self._twttAuth.set_access_token(self._AccssTkn, self._AccssTknSek)
			# forcing an error...
			#self._twttAuth.set_access_token("","")
			self._twttcli = tweepy.API(self._twttAuth)
			self._usrTwtt = self._twttcli.verify_credentials()
		except tweepy.TweepError as e:
			raise ValueError(f"(Twitter authorization: {e.response.text})")
		except:
			raise

		# I 'love' and read documentations :/ ....
		return False if self._usrTwtt == False else True

	def notify(self, msg):
		self._lastStatus = self._twttcli.update_status(msg)
		return self._lastStatus

	def close(self):
		print('twitter close')

class notify(Exception):
	_type      = str('')
	_notifyObj = object()
	_level     = list('')

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

	def cfg(self, c : dict = {}):
		return self._notifyObj.cfg(c)

	def open(self) -> bool:
		return self._notifyObj.open()

	def notify(self, level, msg):
		if level in self._level:
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
