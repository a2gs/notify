#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import notify

a = notify.notify('twitter', ['SystemError', 'Warning', 'Notify'])
#print(a.level())
a.levelAdd(['Debug'])
#print(a.level())
a.open()
