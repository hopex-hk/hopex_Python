from hopex.constant.definition import OrderTradeType, OrderType
from hopex.client.trade import TradeClient

from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)

"""
    create condition order information
    :params
    side: 1:Buy Long, 2:Sell Short, 3:Buy to Close Short, 4:Sell to Close Long
    type: Limit:limit order     Market:market order
    trig_price: Trigger price
    expected_quantity: Preset quantity
    expected_price: Preset price
"""

contract_code = 'BTCUSDT'

# # case condition limit order
res = trade_client.create_condition_order(contract_code=contract_code, side=OrderTradeType.BUY_LONG,
                                          type=OrderType.LIMIT, trig_price=55000,
                                          expected_quantity=10, expected_price=54500)

if res and len(res) and res.get('ret', -1) == 0 and res.get('data', False):
    LogInfo.output("create condition limit order success")
else:
    LogInfo.output("create condition limit order fail:{res}".format(res=res))

# # case condition market order
# res = trade_client.create_condition_order(contract_code=contract_code, side=OrderTradeType.BUY_LONG,
#                                           type=OrderType.MARKET, trig_price=55000,
#                                           expected_quantity=10, expected_price=None)
# if res and len(res) and res.get('ret', -1) == 0 and res.get('data', False):
#     LogInfo.output("create condition market order success")
# else:
#     LogInfo.output("create condition market order fail:{res}".format(res=res))
