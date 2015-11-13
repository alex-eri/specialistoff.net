#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import random

def pwgen(length=15):
    """
    Генератор пароля
    """
    keylist='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password=[]

    while len(password) < length:
        a_char = random.choice(keylist)
        password.append(a_char)
    return ''.join(password)

print pwgen()
