#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import argparse
import os
import re
import subprocess
import sys
import traceback
import json

def main():
    parser = argparse.ArgumentParser(description='Test discovery for Zabbix',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--discovery", dest="discovery", action='store_true', help="Режим обнаружения")
    parser.add_argument('integers', metavar='N', type=int, nargs='*',
        help='an integer for the accumulator')

    args = parser.parse_args()

    if args.discovery:
        data = [
            {"{#T1}": "1","{#T2}": "1"},
            {"{#T1}": "1","{#T2}": "2"},
            {"{#T1}": "2","{#T2}": "1"},
            {"{#T1}": "2","{#T2}": "2"}
            ]
        result = json.dumps({"data": data})
        print result
    else:
        print str(args.integers[0] + args.integers[1])

if __name__ == "__main__":
    try:
        main()
    except Exception, ex:
        traceback.print_exc(file=sys.stdout)
        exit(1)

    exit(0)
