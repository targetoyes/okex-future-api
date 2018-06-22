1.首先，在base目录的settings.py下填写
  api_key =''              
  secret_key = ''                            # 自行填写

2. 如需更换货币类型请修改：
  default = {
    'symbol': 'eos_usd',                   # 自行修改(如: btc_usd ltc_usd eth_usd etc_usd bch_usd)
    'contract_type': 'this_week'           # 自行修改(如: 合约类型: this_week:当周 next_week:下周 quarter:季度)
  }

3.其他说明：
  启动方式： python main.py (默认启动app目录下的test.py)

  选择app下的其他策略脚本: python main.py plan_a     (plan_a.py必须在app目录下存在)

  其他策略请自行在app目录下编写,本项目只提供python的基础api

4.该api无后门,请安心使用。

5.api存在问题请联系我。
