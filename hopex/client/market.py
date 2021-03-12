from hopex.utils.input_checker import *


class MarketClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs:The option of request connection.
           api_key: The public key applied from Hopex.
           secret_key: The private key applied from Hopex.
           url: The URL name like "https://api2.hopex.com".
           init_log: to init logger
        """
        self.__kwargs = kwargs

    def get_kline(self, contract_code: str, end_time: int, start_time: int, interval: str):
        """
        Get kline data  (Maximum 1000 Kline Data)
        :param contract_code:   The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param end_time:    The kline data util end_time     (mandatory)
        :param start_time:  The kline data from start_time   (mandatory)
        :param interval:    The kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :return:    The list of kline data.
        """
        check_symbol(contract_code)
        check_should_not_none(end_time, "end_time")
        check_should_not_none(start_time, "start_time")
        check_should_not_none(interval, "interval")

        params = {
            'contractCode': contract_code,
            'endTime': end_time,
            'startTime': start_time,
            'interval': interval
        }
        from hopex.services.market.get_kline import GetKlineService
        return GetKlineService(params).request(**self.__kwargs)

    def get_market_ticker(self, contract_code: str):
        """
        Get single market
        :param contract_code:   The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :return:    The object of single market data
        """
        check_symbol(contract_code)
        params = {'contractCode': contract_code}
        from hopex.services.market.get_market_ticker import GetMarketTickersService
        return GetMarketTickersService(params).request(**self.__kwargs)

    def get_markets(self) -> list:
        """
        Get all market data
        :return:    all market data
        """
        params = {}
        from hopex.services.market.get_markets import GetMarketsService
        return GetMarketsService(params).request(**self.__kwargs)

    def get_trades(self, contract_code: str, page_size: int = 10) -> list:
        """
        Get the most recent trades
        :param contract_code:   The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param page_size:   page size (optional)
        :return:    The list of trades
        """
        check_symbol(contract_code)
        check_range(page_size, 1, 2000, "page_size")
        params = {
            'contractCode': contract_code,
            'pageSize': page_size
        }
        from hopex.services.market.get_trades import GetTradesService
        return GetTradesService(params).request(**self.__kwargs)

    def post_query_market_depth(self, contract_code: str, page_size: int = 10) -> list:
        """
        Get the market depth
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param page_size:  page size (optional)
        :return: The list of depth
        """
        check_symbol(contract_code)
        check_range(page_size, 1, 2000, "page_size")
        params = {
            "param": {
                'contractCode': contract_code,
                'pageSize': page_size
            }

        }
        from hopex.services.market.post_market_depth import PostQueryMarketDepthService
        return PostQueryMarketDepthService(params).request(**self.__kwargs)
