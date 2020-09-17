# -*- coding: utf-8 -*-


from plugin.extensions import _l
from plugin.settings import ICON_PATH


RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': _l('Click & Copy to Clipboard'),
    'IcoPath': ICON_PATH,
    'JsonRPCAction': {
        'method': 'copy2clipboard',
        'parameters': [],
        'dontHideAfterAction': False
    }
}
