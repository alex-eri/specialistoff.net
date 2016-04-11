#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = 'RemiZOffAlex, eri'
__copyright__ = '(c) RemiZOffAlex'
__license__ = 'MIT'
__email__ = 'remizoffalex@mail.ru'

'''
Генератор конфигурационного файла для сетевых интерфейсов

Пример применения нативных шаблонов
'''

import os
import sys

templates = {"debian": """auto eth0:{i}
iface eth0:{i} inet static
	address {ip}
	netmask 255.255.255.0

""",
"freebsd": '''ifconfig_re0="inet {ip} netmask 255.255.255.0 up"'''}

listip = "192.168.0.2 192.168.0.3"

for i, line in enumerate(listip.strip().split()):
    template=templates["debian"]
    template=template.format(i=i, ip=line)
    print(template)
