from hopex.client.trade import TradeClient

from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
contract_code = "BTCUSDT"
contract_code_list = [contract_code]
task_type_list = list()
trig_type_list = list()
task_status_list = list()
direct = 0
side = 0
start_time = 0
end_time = 0

res = trade_client.req_condition_orders(contract_code_list=contract_code_list, task_type_list=task_type_list,
                                        trig_type_list=trig_type_list, task_status_list=task_status_list,
                                        direct=direct, side=side,
                                        start_time=start_time, end_time=end_time)

if res and len(res) and res.get('ret', -1) == 0:
    task_data = res.get('data', {})
    task_list = task_data.get('result', list())
    task_list = list(filter(lambda x: x['taskStatus'] == 1 if x.get('taskStatus') else False, task_list) if len(
        task_list) else 0)
    task_id_tmp = task_list[0].get('taskId', 0) if len(task_list) else 0

    if task_id_tmp:
        cancel_res = trade_client.cancel_condition_order(contract_code, task_id_tmp)
        if cancel_res and len(cancel_res) and cancel_res.get('ret', -1) == 0 and cancel_res.get('data', False):
            LogInfo.output("cancel condition order {id} done".format(id=task_id_tmp))
        else:
            LogInfo.output_list("cancel condition order fail: {res}".format(res=cancel_res))
else:
    LogInfo.output_list("cancel condition order fail: {res}".format(res=res))
