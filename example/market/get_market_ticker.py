from hopex.client.market import MarketClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

market_client = MarketClient(api_key=t_api_key, secret_key=t_secret_key)

contract_code = 'BTCUSDT'
obj = market_client.get_market_ticker(contract_code=contract_code)
LogInfo.output(obj)
