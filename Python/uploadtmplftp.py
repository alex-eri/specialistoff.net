#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

__author__ = 'RemiZOffAlex'
__copyright__ = '(c) RemiZOffAlex 2015'
__license__ = 'MIT'
__email__ = 'remizoffalex@mail.ru'


import traceback
import argparse
import ftplib
import sys

from jinja2 import Environment, FileSystemLoader

def genfiles(templatename, data, ftpserver, ftpuser, ftppassword):
    j2_env=Environment(loader=FileSystemLoader('./'),
                     trim_blocks=True)
    ftpcon = ftplib.FTP(ftpserver, ftpuser, ftppassword)
    template=j2_env.get_template(templatename).render(data=data)
    template=template.encode('utf-8')
    bio = io.BytesIO(template)
    ftpcon.storbinary('STOR file.txt', bio)
    ftpcon.quit()

def main():
    parser = argparse.ArgumentParser(
        description='Скрипт создания файла из шаблона и отправка его на FTP сервер',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--templatename", dest="templatename", required=True, help="Имя файла шаблона")
    parser.add_argument("--ftpserver", dest="ftpserver", required=True, help="FTP сервер для загрузки")
    parser.add_argument("--ftpuser", dest="ftpuser", required=True, help="Пользователь FTP")
    parser.add_argument("--ftppassword", dest="ftppassword", required=True, help="Пароль FTP")


    args = parser.parse_args()

    data = [] # Данные для передачи в шаблон
    try:
        genfiles(templatename = args.templatename,
            data = data,
            ftpserver = args.ftpserver,
            ftpuser = args.ftpuser,
            ftppassword = args.ftppassword)
    except Exception as ex:
        traceback.print_exc(file=sys.stdout)
        exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        traceback.print_exc(file=sys.stdout)
        exit(1)

    exit(0)
