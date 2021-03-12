from hopex.client.market import MarketClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

market_client = MarketClient(api_key=t_api_key, secret_key=t_secret_key)

contract_code = 'BTCUSDT'
list_obj = market_client.post_query_market_depth(contract_code=contract_code, page_size=10)

LogInfo.output_list(list_obj)
