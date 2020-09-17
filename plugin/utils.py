# -*- coding: utf-8 -*-


def isfloat(value: float):
    flag = False
    if value.isdecimal():
        flag = True
    else:
        value_parts = value.split('.')
        if len(value_parts) == 2 and all(i.isdecimal() for i in value_parts):
            flag = True

    return flag
