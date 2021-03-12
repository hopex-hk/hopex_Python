from hopex.client.trade import TradeClient

from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)

contract_code = 'BTCUSDT'

list_obj = trade_client.get_open_orders(contract_code=contract_code)
LogInfo.output_list(list_obj)
