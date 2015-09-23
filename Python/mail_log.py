##!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import getpass, poplib
import argparse

def main():
    parser = argparse.ArgumentParser(description='Лог подключения к почтовому серверу',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--server", dest="server", help="IP или имя почтового сервера")
    parser.add_argument("--port", dest="port", help="Порт сервера")
    parser.add_argument("--login", dest="login", help="Пользователь")
    parser.add_argument("--password", dest="password", help="Пароль")

    args = parser.parse_args()

    M = poplib.POP3(args.server, args.port)
    M.set_debuglevel(2)
    success = False
    while success == False:
        try:
            M.user(args.login)
            M.pass_(args.password)
        except:
            print("Invalid credentials")
        else:
            print("Successful login")
            success = True
    numMessages = len(M.list()[1])
    print('Всего ' + str(numMessages) + ' писем')
#   for i in range(numMessages):
#       for j in M.retr(i+1)[1]:
#           print(j)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc(file=sys.stdout)
        exit(1)

    exit(0)
