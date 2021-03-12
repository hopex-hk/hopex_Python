from hopex.client.trade import TradeClient

from hopex.constant.definition import Direct
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo
import time

trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key)
# case set long leverage
contract_code = 'BTCUSDT'
direct = Direct.LONG
leverage = 5
obj = trade_client.set_leverage(contract_code=contract_code, direct=direct, leverage=leverage)
LogInfo.output(obj, '==set long leverage==')

# case set short leverage
time.sleep(1)  # api rate limit
contract_code = 'BTCUSDT'
direct = Direct.SHORT
leverage = 10
obj = trade_client.set_leverage(contract_code=contract_code, direct=direct, leverage=leverage)
LogInfo.output(obj, '==set short leverage==')
