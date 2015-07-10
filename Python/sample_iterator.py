##!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import sys
import traceback

class DataProvider():
    def __init__(self):
        """
        Инициализация класса
        """
        self.mylist = [1, 2, 3, 4, 5]
        self.iterator = iter(self.mylist)

    def __iter__(self):
        """
        Инициализация итератора
        """
        return self

    def next(self):
        """
        Выборка элемента
        """
        result = self.iterator.next()
        return result

def main():
    dataProv = DataProvider()
    for i in dataProv:
        print i

if __name__ == "__main__":
    try:
        main()
    except Exception, ex:
        traceback.print_exc(file=sys.stdout)
        exit(1)

    exit(0)
