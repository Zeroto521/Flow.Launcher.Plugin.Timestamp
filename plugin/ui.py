# -*- coding: utf-8 -*-

import copy
import time

import pyperclip

from plugin.extensions import _l
from plugin.templates import RESULT_TEMPLATE
from plugin.utils import isfloat
from plugin.wox import Wox


class Main(Wox):

    def query(self, param: str = ''):
        result = []
        param = param.strip()
        if not param:
            stamp = int(time.time())
            date = time.strftime("%Y-%m-%d", time.localtime(stamp))
            nowt = time.strftime("%H:%M:%S", time.localtime(stamp))

            result.append(self.genformat(stamp, _l('Timestamp')))
            result.append(self.genformat(date, _l('Date')))
            result.append(self.genformat(nowt, _l('Time')))
            result.append(self.genformat(f'{date} {nowt}', _l('Date & Time')))
        else:
            if isfloat(param):
                local_time = time.localtime(float(param))
                res = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
            else:
                # FIXME: find some package to pare any time format.
                if ":" in param:
                    colon_num = param.count(':')
                    if colon_num == 2:
                        time_data = time.strptime(param, "%Y-%m-%d %H:%M:%S")
                    elif colon_num == 1:
                        time_data = time.strptime(param, "%Y-%m-%d %H:%M")
                else:
                    time_data = time.strptime(param, "%Y-%m-%d")
                res = time.mktime(time_data)
            result.append(self.genformat(res, _l('Result')))

        return result

    def copy2clipboard(self, value):
        pyperclip.copy(str(value).strip())

    @staticmethod
    def genformat(value, string: str):
        time_format = copy.deepcopy(RESULT_TEMPLATE)
        time_format['Title'] = "{}：{}".format(string, value)
        time_format['JsonRPCAction']['parameters'].append(value)

        return time_format
