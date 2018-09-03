"""
create by 维尼的小熊 on 2018/8/30

"""

__autor__ = 'yasin'

import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text