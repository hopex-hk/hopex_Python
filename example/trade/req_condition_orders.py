from hopex.client.trade import TradeClient

from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)

"""
    The condition orders information
    :params
    contract_code_list:   Contract List, Being blank to search all contracts
    task_type_list:   1:Buy Long, 2:Sell Short, 3:Buy to Close Short, 4:Sell to Close Long, Being blank to search all
    trig_type_list:   1:Market Price 2:Faire Price,Being blank to search all
    task_status_list: 1: Untriggered 2.Canceled 3.Order Submitted 4.Trigger failed, Being blank to search all
    direct: 1 LONG,2 SHORT,0:search all
    side: 1:Sell 2Buy,0:search all
    start_time:  0:search all,Start Time Stamp(Unit microsecond)
    end_time:  0:search all,End Time Stamp(Unit microsecond)
"""

# case query condition orders all
contract_code_list = ['BTCUSDT', 'ETHUSDT']
task_type_list = []
trig_type_list = []
task_status_list = []
direct = 0
side = 0
start_time = 0
end_time = 0

list_obj = trade_client.req_condition_orders(contract_code_list=contract_code_list, task_type_list=task_type_list,
                                             trig_type_list=trig_type_list,
                                             task_status_list=task_status_list, direct=direct, side=side,
                                             start_time=start_time,
                                             end_time=end_time)

LogInfo.output_list(list_obj, "==query condition orders all==")
