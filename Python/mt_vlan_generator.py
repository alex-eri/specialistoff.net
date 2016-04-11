#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = 'RemiZOffAlex, Eri'
__copyright__ = '(c) RemiZOffAlex'
__license__ = 'MIT'
__email__ = 'remizoffalex@mail.ru'

'''
Генератор команд для MikroTik
Для тех, у кого много VLAN

Пример применения шаблонов, распаковка звездочками
'''

import os
import sys

template = """/interface vlan
add interface=bridge-local name=vlan{id} vlan-id={id}
/ip address
add interface=vlan{id} address={ip}/24

"""

vlans = [{'id': 70, 'ip': '192.168.0.2'},
{'id': 80, 'ip': '192.168.0.3'}]

for item in vlans:
    conf=template.format(**item)
    print(conf)
