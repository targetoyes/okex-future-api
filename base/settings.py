#!/usr/bin/env python
# -*- coding: utf-8 -*-

SCRIPT_SELECT = 'test'    # 使用app中的哪个文件

api_key =''                                # 自行填写
secret_key = ''                            # 自行填写
main_url = 'https://www.okex.com/api/v1/'

default = {
    'symbol': 'eos_usd',                   # 自行修改
    'contract_type': 'this_week'           # 自行修改
}

API_GET_LIST = {
    'future_ticker': 'future_ticker.do',
    'future_depth': 'future_depth.do',
    'future_trades': 'future_trades.do',
    'future_index': 'future_index.do',
    'exchange_rate': 'exchange_rate.do',
    'future_estimated_price': 'future_estimated_price.do',
    'future_kline': 'future_kline.do',
    'future_hold_amount': 'future_hold_amount.do',
    'future_price_limit': 'future_price_limit.do'
}

API_POST_LIST = {
    'future_userinfo': 'future_userinfo.do',
    'future_position': 'future_position.do',
    'future_trade': 'future_trade.do',
    'future_batch_trade': 'future_batch_trade.do',
    'future_cancel': 'future_cancel.do',
    'future_order_info': 'future_order_info.do',
    'future_orders_info': 'future_orders_info.do',
    'future_userinfo_4fix': 'future_userinfo_4fix.do',
    'future_position_4fix': 'future_position_4fix.do',
    'future_explosive': 'future_explosive.do',
    'future_devolve': 'future_devolve.do'
}
