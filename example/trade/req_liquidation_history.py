from hopex.client.trade import TradeClient
from hopex.constant.definition import OrderSide
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)

"""
    The liquidation_history information
    :params
    contract_code_list:   Contract List, Being blank to search all contracts
    side: 1:Sell 2Buy,0:search all
"""

contract_code_list = ['BTCUSDT', 'ETHUSDT']

page = 1
limit = 10

list_obj = trade_client.req_liquidation_history(contract_code_list=contract_code_list, side=0, page=page, limit=limit)
# list_obj = trade_client.req_liquidation_history(contract_code_list=contract_code, OrderSide.BUY, page, limit)
# list_obj = trade_client.req_liquidation_history(contract_code_list=contract_code, OrderSide.SELL, page, limit)

LogInfo.output_list(list_obj)
