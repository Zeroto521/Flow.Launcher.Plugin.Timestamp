# -*- coding: utf-8 -*-

import copy
import time

import pyperclip

from plugin.extensions import _l
from plugin.templates import RESULT_TEMPLATE
from plugin.wox import Wox


class Main(Wox):

    def query(self, param: str = ''):
        result = []
        param = param.strip()

        stamp = int(time.time())
        date = time.strftime("%Y-%m-%d", time.localtime(stamp))
        nowt = time.strftime("%H:%M:%S", time.localtime(stamp))

        result.append(self.genformat(stamp, _l('Timestamp')))
        result.append(self.genformat(date, _l('Date')))
        result.append(self.genformat(nowt, _l('Time')))
        result.append(self.genformat(f'{date} {nowt}', _l('Date & Time')))

        return result

    def copy2clipboard(self, value):
        pyperclip.copy(str(value).strip())

    @staticmethod
    def genformat(value, string: str):
        time_format = copy.deepcopy(RESULT_TEMPLATE)
        time_format['Title'] = "{}：{}".format(string, value)
        time_format['JsonRPCAction']['parameters'].append(value)

        return time_format
