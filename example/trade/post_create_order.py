from hopex.client.trade import TradeClient

from hopex.constant.definition import OrderTradeType
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)

"""
    create order information
    :params
    side: 1:Buy Long, 2:Sell Short, 3:Buy to Close Short, 4:Sell to Close Long
    order_Quantity: Order Quantity
    order_Price: integral multiple of tick size. If not filled, it means place a market order
"""

# # # # case Limit Order
contract_code = 'BTCUSDT'

# # BUY_LONG
res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.BUY_LONG, order_quantity=10,
                                order_price=40000)
if res and len(res) and res.get('ret', -1) == 0:
    order_id = res.get('data', 0)
    LogInfo.output("created order id : {id}".format(id=order_id))
    cancel_res = trade_client.cancel_order(contract_code=contract_code, order_id=order_id)
    if cancel_res and len(cancel_res) and res.get('ret', -1) == 0 and res.get('data', False):
        LogInfo.output("cancel order {id} done".format(id=order_id))
    else:
        LogInfo.output_list("cancel order fail: {res}".format(res=cancel_res))
else:
    LogInfo.output_list("create order fail: {res}".format(res=res))

# # SELL_TO_CLOSE_LONG
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.SELL_TO_CLOSE_LONG,
#                                 order_quantity=10, order_price=55000)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     LogInfo.output("created order id : {id}".format(id=order_id))
#     cancel_res = trade_client.cancel_order(contract_code=contract_code, order_id=order_id)
#     if cancel_res and len(cancel_res) and res.get('ret', -1) == 0 and res.get('data', False):
#         LogInfo.output("cancel order {id} done".format(id=order_id))
#     else:
#         LogInfo.output_list("cancel order fail: {res}".format(res=cancel_res))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))


# # SELL_SHORT
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.SELL_SHORT,
#                                 order_quantity=10, order_price=60000)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     LogInfo.output("created order id : {id}".format(id=order_id))
#     cancel_res = trade_client.cancel_order(contract_code=contract_code, order_id=order_id)
#     if cancel_res and len(cancel_res) and res.get('ret', -1) == 0 and res.get('data', False):
#         LogInfo.output("cancel order {id} done".format(id=order_id))
#     else:
#         LogInfo.output_list("cancel order fail: {res}".format(res=cancel_res))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))


# # BUY_TO_CLOSE_SHORT
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.BUY_TO_CLOSE_SHORT,
#                                 order_quantity=10, order_price=50000)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     LogInfo.output("created order id : {id}".format(id=order_id))
#     cancel_res = trade_client.cancel_order(contract_code=contract_code, order_id=order_id)
#     if cancel_res and len(cancel_res) and res.get('ret', -1) == 0 and res.get('data', False):
#         LogInfo.output("cancel order {id} done".format(id=order_id))
#     else:
#         LogInfo.output_list("cancel order fail: {res}".format(res=cancel_res))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))


# # # # case Market Order


# # BUY_LONG Market Order
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.BUY_LONG, order_quantity=10,
#                                 order_price=None)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     if order_id:
#         LogInfo.output("created order id : {id}".format(id=order_id))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))
#
#
# # SELL_TO_CLOSE_LONG Market Order
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.SELL_TO_CLOSE_LONG,
#                                 order_quantity=10, order_price=None)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     if order_id:
#         LogInfo.output("created order id : {id}".format(id=order_id))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))
#
#
# # SELL_SHORT Market Order
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.SELL_SHORT,
#                                 order_quantity=10, order_price=None)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     if order_id:
#         LogInfo.output("created order id : {id}".format(id=order_id))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))
#
#
# # BUY_TO_CLOSE_SHORT Market Order
# res = trade_client.create_order(contract_code=contract_code, side=OrderTradeType.BUY_TO_CLOSE_SHORT,
#                                 order_quantity=10, order_price=None)
#
# if res and len(res) and res.get('ret', -1) == 0:
#     order_id = res.get('data', 0)
#     LogInfo.output("created order id : {id}".format(id=order_id))
# else:
#     LogInfo.output_list("create order fail: {res}".format(res=res))
