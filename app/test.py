#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from base.service import *
from time import sleep

def main():
    ok = okexFuture()

    ################ GET ##################
    print('# ============= 获取OKEx合约行情 ================= #')
    print(ok.future_ticker())

    print('# ============= 获取OKEx合约深度信息 ================= #')
    print(ok.future_depth())

    print('# ============= 获取OKEx合约指数信息 ================= #')
    print(ok.future_index())

    print('# ============= 获取美元人民币汇率 ================= #')
    print(ok.exchange_rate())

    print('# ============= 获取交割预估价 ================= #')
    print(ok.future_estimated_price())

    print('# ============= 获取OKEx合约K线信息 ================= #')
    print(ok.future_kline(ctype='1day', since='2018-06-21 00:00:00'))
    print(ok.future_kline(ctype='1day', since=1529596400000))

    print('# ============= 获取当前可用合约总持仓量 ================= #')
    print(ok.future_hold_amount())

    print('# ============= 获取合约最高限价和最低限价 ================= #')
    print(ok.future_price_limit())

    ################ POST #################
    print('# ============= 获取OKEx合约账户信息(全仓) ================= #')
    print(ok.future_userinfo())

    print('# ============= 用户持仓获取OKEX合约账户信息 （全仓） ================= #')
    print(ok.future_position())

    print('# ============= 下单并取消 ================= #')
    res = ok.future_trade(price=1, amount=1, ctype=1, lever_rate=10)
    print(res)
    if res['result']:
        order_id = res['order_id']
        res = ok.future_cancel(order_id=order_id)
        print(res)

    print('# ============= 批量下单并查看信息后取消 ================= #')

    orders_data = [{'price': 1, 'amount': 1, 'type': 1}, {'price': 1.2, 'amount': 1, 'type': 1}]
    res = ok.future_batch_trade(orders_data=orders_data, lever_rate=10)
    print(res)
    res = ok.future_order_info(order_id='-1')
    print(res)
    if res['result']:
        for trade in res['orders']:
            if trade['order_id'] != -1:
                order_id = trade['order_id']
                sleep(0.5)
                res1 = ok.future_order_info(order_id=order_id)
                print(res1)
                res = ok.future_cancel(order_id=order_id)
                print(res)

    print('# ============= 获取逐仓合约账户信息 ================= #')
    print(ok.future_userinfo_4fix())

    print('# ============= 逐仓用户持仓查询 ================= #')
    print(ok.future_position_4fix())

    print('# ============= 获取合约爆仓单 ================= #')
    print(ok.future_explosive())

    print('# ============= 个人账户资金划转 ================= #')
    print(ok.future_devolve(ctype=2, amount=0.5))
    print(ok.future_devolve(ctype=1, amount=0.5))
