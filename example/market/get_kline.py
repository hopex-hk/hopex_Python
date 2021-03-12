from hopex.constant.definition import CandlestickInterval
from hopex.client.market import MarketClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

import time

market_client = MarketClient()

contract_code = 'BTCUSDT'
end_time = int(time.time())
before_30min = end_time - 60 * 30
before_24h = end_time - 60 * 60 * 24
before_1week = end_time - 60 * 60 * 24 * 7
before_30day = end_time - 60 * 60 * 24 * 30
before_60day = end_time - 60 * 60 * 24 * 60
before_1year = end_time - 60 * 60 * 24 * 365

# list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_30min,
#                                    interval=CandlestickInterval.MIN1)

list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_24h,
                                   interval=CandlestickInterval.MIN5)

# list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_24h,
#                                    interval=CandlestickInterval.HOUR1)

# list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_1week,
#                                    interval=CandlestickInterval.DAY1)

# list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_30day,
#                                    interval=CandlestickInterval.WEEK1)

# list_obj = market_client.get_kline(contract_code=contract_code, end_time=end_time, start_time=before_1year,
#                                    interval=CandlestickInterval.MON1)

LogInfo.output_list(list_obj)
