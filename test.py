# -*- coding: utf-8 -*-

from pprint import pprint

from plugin import Main


if __name__ == '__main__':
    t = Main().query()
    pprint(t)
