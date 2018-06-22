#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .settings import default, API_GET_LIST, API_POST_LIST
from .utils import BaseRequest
import inspect
from datetime import datetime
import json

class okexFuture(object):
    def __init__(self):
        self.R = BaseRequest()
    
    ########### 使用GET方法##########
    def future_ticker(self, 
            symbol=default['symbol'], 
            contract_type=default['contract_type']):
        """
        获取OKEx合约行情:
        ======================
        buy:买一价
        contract_id:合约ID
        high:最高价
        last:最新成交价
        low:最低价
        sell:卖一价
        unit_amount:合约面值
        vol:成交量(最近的24小时)
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {'symbol': symbol, 'contract_type': contract_type}
        r_data = self.R.get(url, params=params)
        return r_data

    def future_depth(self,
            symbol=default['symbol'],
            contract_type=default['contract_type']):
        """
        获取OKEx合约深度信息:
        =======================
        asks :卖方深度
        bids :买方深度
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {'symbol': symbol, 'contract_type': contract_type}
        r_data = self.R.get(url, params=params)
        return r_data

    def future_index(self,
            symbol=default['symbol']):
        """
        获取OKEx合约指数信息:        
        ====================
        future_index :指数
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {'symbol': symbol}
        r_data = self.R.get(url, params=params)
        return r_data

    def exchange_rate(self):
        """
        获取美元人民币汇率:        
        ====================
        rate：美元-人民币汇率
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {}
        r_data = self.R.get(url, params=params)
        return r_data

    def future_estimated_price(self,
            symbol=default['symbol']):
        """
        获取交割预估价:        
        ====================
        forecast_price:交割预估价  注意：交割预估价只有交割前三小时返回
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {'symbol': symbol}
        r_data = self.R.get(url, params=params)
        return r_data

    def future_kline(self,
            symbol=default['symbol'],
            contract_type=default['contract_type'],
            ctype='1min', # 1min/3min/5min/15min/30min/1day/3day/1week/1hour/2hour/4hour/6hour/12hour
            size=0,  # 指定获取数据的条数
            since='2018-01-01 00:00:00'  # 时间戳（eg：1417536000000或者’2018-01-01 00:00:00‘）。 返回该时间戳以后的数据
        ):
        """
        获取OKEx合约K线信息:        
        ====================
        [
            1440308760000,  时间戳
            233.38,     开
            233.38,     高
            233.27,     低
            233.37,     收
            186,        交易量
            79.70234956     交易量转化BTC或LTC数量
        ]
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        if isinstance(since, int):
            since = str(since)
        else:
            try:
                since = int(datetime.strptime(since, '%Y-%m-%d %H:%M:%S').strftime("%s"))*1000
            except:
                return {'result': False, 'msg': 'since时间格式不正确!'}
        params = {
            'symbol': symbol,
            'contract_type': contract_type,
            'type': ctype,
            'size': size,
            'since': since
        }
        r_data = self.R.get(url, params=params)
        return r_data

    def future_hold_amount(self,
            symbol=default['symbol'],
            contract_type=default['contract_type']):
        """
        获取当前可用合约总持仓量:
        =======================
        amount:总持仓量（张）
        contract_name:合约名
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {'symbol': symbol, 'contract_type': contract_type}
        r_data = self.R.get(url, params=params)
        return r_data

    def future_price_limit(self,
            symbol=default['symbol'],
            contract_type=default['contract_type']):
        """
        获取合约最高限价和最低限价:
        =======================
        high :最高买价
        low :最低卖价
        """
        url_key = inspect.stack()[0][3]
        url = API_GET_LIST[url_key]
        params = {'symbol': symbol, 'contract_type': contract_type}
        r_data = self.R.get(url, params=params)
        return r_data

    ########### 使用POST方法##########
    def future_userinfo(self, 
           symbol=default['symbol']):
        """
        获取OKEx合约账户信息(全仓):
        =======================
        account_rights:账户权益
        keep_deposit：保证金
        profit_real：已实现盈亏
        profit_unreal：未实现盈亏
        risk_rate：保证金率
        """
        symbol = symbol.split('_')[0]
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        c_data = self.R.post(url)
        if c_data['result']:
            r_data = c_data['info'][symbol]
            r_data['result'] = True
            return r_data

    def future_position(self, 
            symbol=default['symbol'], 
            contract_type=default['contract_type']):
        """
        获取用户持仓获取OKEX合约账户信息 （全仓）:
        ================================
        buy_amount(double):多仓数量
        buy_available:多仓可平仓数量
        buy_price_avg(double):开仓平均价
        buy_price_cost(double):结算基准价
        buy_profit_real(double):多仓已实现盈余
        contract_id(long):合约id
        create_date(long):创建日期
        lever_rate:杠杆倍数
        sell_amount(double):空仓数量
        sell_available:空仓可平仓数量
        sell_price_avg(double):开仓平均价
        sell_price_cost(double):结算基准价
        sell_profit_real(double):空仓已实现盈余
        symbol:btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
        contract_type:合约类型
        force_liqu_price:预估爆仓价
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol, 'contract_type': contract_type}
        r_data = self.R.post(url, data=data)
        return r_data

    def future_trade(self,
            symbol=default['symbol'],
            contract_type=default['contract_type'],
            price=100000000000,               # 价格
            amount=10000000000000,            # 委托数量
            ctype=1,                   # 1:开多 2:开空 3:平多 4:平空
            match_price=0,            # 是否为对手价 0:不是 1:是 ,当取值为1时,price无效
            lever_rate=10,            # 杠杆倍数，下单时无需传送，系统取用户在页面上设置的杠杆倍数。且“开仓”若有10倍多单，就不能再下20倍多单             
        ):
        """
        合约下单:
        ================================
        order_id ： 订单ID
        result： true代表成功返回
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol, 
                'contract_type': contract_type,
                'price': str(price),
                'amount': str(amount),
                'type': str(ctype),
                'match_price': str(match_price),
                'lever_rate': str(lever_rate)
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_batch_trade(self,
            symbol=default['symbol'],
            contract_type=default['contract_type'],
            lever_rate=10,            # 杠杆倍数，下单时无需传送，系统取用户在页面上设置的杠杆倍数。且“开仓”若有10倍多单，就不能再下20倍多单     
            orders_data=[]               # JSON类型的字符串 例：[{price:5,amount:2,type:1,match_price:1},{price:2,amount:3,type:1,match_price:1}] 最大下单量为5，price,amount,type,match_price参数参考future_trade接口中的说明
        ):
        """
        批量下单:
        ================================
        result:订单交易成功或失败
        order_id:订单ID
        备注:
             只要其中任何一单下单成功就返回true
             返回的结果数据和orders_data提交订单数据顺序一致
             如果下单失败：order_id为-1，error_code为错误代码
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol, 
                'contract_type': contract_type,
                'lever_rate': str(lever_rate),
                'orders_data': json.dumps(orders_data)
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_cancel(self,
            symbol=default['symbol'],
            contract_type=default['contract_type'],
            order_id=''                  # 订单ID(多个订单ID中间以","分隔,一次最多允许撤消5个订单)
        ):
        """
        取消合约订单:
        =======================
        result:订单交易成功或失败(用于单笔订单)
        order_id:订单ID(用于单笔订单)
        success:成功的订单ID(用于多笔订单)
        error:失败的订单ID后跟失败错误码(用户多笔订单)
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol,
                'contract_type': contract_type,
                'order_id': order_id
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_order_info(self,
           symbol=default['symbol'], 
           contract_type=default['contract_type'],
           status='1',                # 查询状态 1:未完成的订单 2:已经完成的订单
           order_id='-1',             # 订单ID -1:查询指定状态的订单，否则查询相应订单号的订单
           current_page='1',          # 当前页数
           page_length='20'           # 每页获取条数，最多不超过50
        ):
        """ 
        获取合约订单信息:
        =======================
        amount: 委托数量
        contract_name: 合约名称
        create_date: 委托时间
        deal_amount: 成交数量
        fee: 手续费
        order_id: 订单ID
        price: 订单价格
        price_avg: 平均价格
        status: 订单状态(0等待成交 1部分成交 2全部成交 -1撤单 4撤单处理中 5撤单中)
        symbol: btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
        type: 订单类型 1：开多 2：开空 3：平多 4： 平空
        unit_amount:合约面值
        lever_rate: 杠杆倍数  value:10\20  默认10 
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol,
                'contract_type': contract_type,
                'status': status,
                'order_id': order_id,
                'current_page': current_page,
                'page_length': page_length
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_orders_info(self,
           symbol=default['symbol'],
           contract_type=default['contract_type'],
           order_id=''             # 订单ID(多个订单ID中间以","分隔,一次最多允许查询50个订单)
        ):
        """ 
        批量获取合约订单信息:
        =======================
        amount: 委托数量
        contract_name: 合约名称
        create_date: 委托时间
        deal_amount: 成交数量
        fee: 手续费
        order_id: 订单ID
        price: 订单价格
        price_avg: 平均价格
        status: 订单状态(0等待成交 1部分成交 2全部成交 -1撤单 4撤单处理中 5撤单中)
        symbol: btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
        type: 订单类型 1：开多 2：开空 3：平多 4： 平空
        unit_amount:合约面值
        lever_rate: 杠杆倍数  value:10\20  默认10 
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol,
                'contract_type': contract_type,
                'order_id': order_id
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_userinfo_4fix(self):
        """ 
        获取逐仓合约账户信息:
        =======================
        balance:账户余额
        available:合约可用
        balance:账户(合约)余额
        bond:固定保证金
        contract_id:合约ID
        contract_type:合约类别
        freeze:冻结
        profit:已实现盈亏
        unprofit:未实现盈亏
        rights:账户权益
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {}
        r_data = self.R.post(url, data=data)
        return r_data

    def future_position_4fix(self,
           symbol=default['symbol'],
           contract_type=default['contract_type'],
           ctype='1'   # 默认返回10倍杠杆持仓 ctype=1 返回全部持仓数据
        ):
        """ 
        逐仓用户持仓查询:
        =======================
        buy_amount:多仓数量
        buy_available:多仓可平仓数量 
        buy_bond:多仓保证金
        buy_flatprice:多仓强平价格
        buy_profit_lossratio:多仓盈亏比
        buy_price_avg:开仓平均价
        buy_price_cost:结算基准价
        buy_profit_real:多仓已实现盈余
        contract_id:合约id
        contract_type:合约类型
        create_date:创建日期
        sell_amount:空仓数量
        sell_available:空仓可平仓数量 
        sell_bond:空仓保证金
        sell_flatprice:空仓强平价格
        sell_profit_lossratio:空仓盈亏比
        sell_price_avg:开仓平均价
        sell_price_cost:结算基准价
        sell_profit_real:空仓已实现盈余
        symbol:btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
        lever_rate: 杠杆倍数
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol,
                'contract_type': contract_type,
                'type': ctype
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_explosive(self,
           symbol=default['symbol'],
           contract_type=default['contract_type'],
           status='0', # 状态 0：最近7天未成交 1:最近7天已成交
           current_page=1, # 当前页数索引值
           page_number=1, # 当前页数(使用page_number时current_page失效，current_page无需传)
           page_length=20, # 每页获取条数，最多不超过50
        ):
        """ 
        获取合约爆仓单:
        =======================
        amount:委托数量（张）
        create_date:创建时间
        loss:穿仓用户亏损
        price:委托价格
        type：交易类型 1：买入开多 2：卖出开空 3：卖出平多 4：买入平空
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol,
                'contract_type': contract_type,
                'status': status,
                'current_page': current_page,
                'page_number': page_number,
                'page_length': page_length
        }
        r_data = self.R.post(url, data=data)
        return r_data

    def future_devolve(self,
           symbol=default['symbol'],
           ctype=2, # 划转类型。1：币币转合约 2：合约转币币
           amount=1000000   # 划转币的数量
        ):
        """ 
        个人账户资金划转:
        =======================
        result:划转结果。若是划转失败，将给出错误码提示。
        """
        url_key = inspect.stack()[0][3]
        url = API_POST_LIST[url_key]
        data = {'symbol': symbol,
                'type': str(ctype),
                'amount': str(amount)
        }
        r_data = self.R.post(url, data=data)
        return r_data
    

if __name__ == '__main__':
    ok = okexFuture()
    print(ok.future_ticker())
    print(ok.future_userinfo())
    print(ok.future_position())
