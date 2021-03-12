from hopex.client.trade import TradeClient

from hopex.constant.test import t_api_key, t_secret_key
from hopex.constant.definition import OrderTradeType
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
contract_code = 'BTCUSDT'
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
