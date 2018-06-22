#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import hashlib
from urllib.parse import urlencode

from .settings import api_key, secret_key, main_url


class BaseRequest(object):
    def __init__(self):
        self.headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
        }
        self.sign = {}

    def create_sign(self, params):
        sign = ''
        for key in sorted(params.keys()):
            sign += key + '=' + str(params[key]) +'&'
        data = sign + 'secret_key=' + secret_key

        return hashlib.md5(data.encode('utf8')).hexdigest().upper()

    def get(self, url, params={}):
        url = main_url + url 
        try:
            res = requests.get(url, params=params, headers=self.headers, timeout=5)
            if res.status_code == 200:
                return res.json()
            else:
                print(res.text, res.status_code)
                return None
        except Exception as e:
            print(e)
            return None

    def post(self, url, params={}, data={}):
        data['api_key'] = api_key
        data['sign'] = self.create_sign(data)
        url = main_url + url 
        try:
            res = requests.post(url, params=params, data=data, headers=self.headers, timeout=5)
            if res.status_code == 200:
                r_data = res.json()
                return r_data
            else:
                print(res.text, res.status_code)
                return None
        except Exception as e:
            print(e)
            return None

if __name__ == '__main__':
    url = 'future_ticker.do'
    params = {'symbol': 'eos_usd', 'contract_type': 'this_week'}
    R = BaseRequest()
    r_data = R.get(url, params=params)
    print(r_data)
    
    url = 'future_userinfo.do'
    r_data = R.post(url)
    print(r_data)
    url = 'future_position.do'
    r_data = R.post(url, data={'symbol': 'eos_usd', 'contract_type': 'this_week'})
    print(r_data)
