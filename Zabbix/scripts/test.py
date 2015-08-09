#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import argparse
import os
import re
import subprocess
import sys
import traceback
import json

parser = argparse.ArgumentParser(description='Test discovery for Zabbix',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--discovery", dest="discovery", action='store_true', help="Режим обнаружения")
parser.add_argument('integers', metavar='N', type=int, nargs='*',
    help='an integer for the accumulator')

args = parser.parse_args()

if args.discovery:
    str_jdump = '{"data": ['
    str_jdump += '{"{#T1}": "1","{#T2}": "1"},'
    str_jdump += '{"{#T1}": "1","{#T2}": "2"},'
    str_jdump += '{"{#T1}": "2","{#T2}": "1"},'
    str_jdump += '{"{#T1}": "2","{#T2}": "2"}'
    str_jdump += ']}'
    jdump = json.loads(str_jdump)
    gf = json.dumps(jdump, indent=4)
    print gf
else:
    print str(args.integers[0] + args.integers[1])
