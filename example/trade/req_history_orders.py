from hopex.constant.definition import OrderSide
from hopex.client.trade import TradeClient

from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo
import time

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)

"""
    The history orders information
    :params
    contract_code_list:   Contract List, Being blank to search all contracts
    type_list:   1.Limit Price to Open 2.Market Price to Open 3.Limit Price to Close 4.Market Price to Close 
                5.Limit Price Close Partially Complete 6.Market Price Close Partially Complete
    side: 1:Sell 2Buy,0:search all
    start_time:  0:search all,Start Time Stamp(Unit microsecond)
    end_time:  0:search all,End Time Stamp(Unit microsecond)
"""

# case  query history orders all
contract_code_list = ['BTCUSDT', 'ETHUSDT']
type_list = []
side = 0  # 0:no limit
start_time = 0
end_time = 0
page = 1
limit = 10
list_obj = trade_client.req_history_orders(contract_code_list=contract_code_list, type_list=type_list, side=side,
                                           start_time=start_time,
                                           end_time=end_time, page=page, limit=limit)
LogInfo.output_list(list_obj, '==query history orders all==')

# case  query history orders by side type
time.sleep(1)  # api rate limit
type_list = [1, 2]
list_obj = trade_client.req_history_orders(contract_code_list=contract_code_list, type_list=type_list, side=side,
                                           start_time=start_time,
                                           end_time=end_time, page=page, limit=limit)
LogInfo.output_list(list_obj, '==query history orders by type==')

# case  query history orders by side BUY
time.sleep(1)  # api rate limit
type_list = []
side = OrderSide.BUY

list_obj = trade_client.req_history_orders(contract_code_list=contract_code_list, type_list=type_list, side=side,
                                           start_time=start_time,
                                           end_time=end_time, page=page, limit=limit)
LogInfo.output_list(list_obj, '==query history orders by side BUY==')

# case  query history orders by side SELL
time.sleep(1)  # api rate limit
type_list = []
side = OrderSide.SELL

list_obj = trade_client.req_history_orders(contract_code_list=contract_code_list, type_list=type_list, side=side,
                                           start_time=start_time,
                                           end_time=end_time, page=page, limit=limit)
LogInfo.output_list(list_obj, '==query history orders by side SELL==')

# case  query history orders by time
time.sleep(1)  # api rate limit
type_list = []
side = 0
end_time = int(time.time())
start_time = end_time - 60 * 60 * 24  # before 1 day
list_obj = trade_client.req_history_orders(contract_code_list=contract_code_list, type_list=type_list, side=side,
                                           start_time=start_time,
                                           end_time=end_time, page=page, limit=limit)
LogInfo.output_list(list_obj, '==query history orders by time==')
