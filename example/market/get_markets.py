from hopex.client.market import MarketClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

market_client = MarketClient(api_key=t_api_key, secret_key=t_secret_key)

list_obj = market_client.get_markets()

LogInfo.output_list(list_obj)
