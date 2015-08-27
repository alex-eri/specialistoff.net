##!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import base64
import uuid
import hashlib

def get_hash_password(password, salt = None):
    """
    Получить хеш пароля SHA-512
    """
    if salt == None:
        salt = uuid.uuid4().hex
    text = password.encode('utf-8') + salt.encode('utf-8')
    h = hashlib.sha512()
    h.update(text)
    return str(h.hexdigest())

print(get_hash_password('password'))
print(get_hash_password('password', 'salt'))
