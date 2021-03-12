from typing import Optional

from hopex.constant.definition import *
from hopex.utils.input_checker import *


class TradeClient(object):

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

    def get_open_orders(self, contract_code: str):
        """
        Get user open orders
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :return:The list of open orders
        """
        check_symbol(contract_code)
        params = {
            'contractCode': contract_code
        }
        from hopex.services.trade.get_open_orders import GetOpenOrdersService
        return GetOpenOrdersService(params).request(**self.__kwargs)

    def get_positions(self):
        """
        Get user all positions
        :return: The list of user positions
        """
        params = {}
        from hopex.services.trade.get_positions import GetPositionsService
        return GetPositionsService(params).request(**self.__kwargs)

    def cancel_condition_order(self, contract_code: str, task_id: int):
        """
        Cancel condition order
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param task_id: The taskId of condition order (mandatory)
        :return: bool, true means canceling condition order is successful
        """
        check_symbol(contract_code)
        check_should_not_none(task_id, "task_id")
        params = {
            "param": {
                "contractCode": contract_code,
                "taskId": task_id
            }
        }

        from hopex.services.trade.post_cancel_condition_order import CancelConditionOrderService
        return CancelConditionOrderService(params).request(**self.__kwargs)

    def cancel_order(self, contract_code: str, order_id: int):
        """
        Cancel order
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param order_id: The orderId of open order (mandatory)
        :return: bool, true means canceling order is successful
        """
        check_symbol(contract_code)
        check_should_not_none(order_id, "order_id")
        params = {
            "contractCode": contract_code,
            "orderId": order_id
        }
        from hopex.services.trade.post_cancel_order import CancelOrderService
        return CancelOrderService(params).request(**self.__kwargs)

    def create_condition_order(self, contract_code: str, side: int, type: str, trig_price: float,
                               expected_quantity: int, expected_price: Optional[float]):
        """
        Create condition order
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param side:    1:Buy Long, 2:Sell Short, 3:Buy to Close Short, 4:Sell to Close Long    (mandatory)
        :param type:    Limit:limit order Market:market order   (mandatory)
        :param trig_price:  Trigger price   (mandatory)
        :param expected_quantity:  Preset quantity  (mandatory)
        :param expected_price:  Preset price    (optional, limit order:mandatory, market order: no)
        :return:bool,true means placing condition order is successful
        """
        check_symbol(contract_code)
        check_range(side, 1, 4, "side")
        check_in_list(type, [OrderType.LIMIT, OrderType.MARKET], "type")
        check_should_not_none(trig_price, "trig_price")
        check_should_not_none(expected_quantity, "expected_quantity")

        params = {
            "param": {
                "contractCode": contract_code,
                "side": side,
                "type": type,
                "trigPrice": trig_price,
                "expectedQuantity": expected_quantity,
                "expectedPrice": expected_price
            }
        }
        from hopex.services.trade.post_create_condition_order import CreateConditionOrderService
        return CreateConditionOrderService(params).request(**self.__kwargs)

    def create_order(self, contract_code: str, side: int, order_quantity: int, order_price: Optional[float]):
        """
        Create order
        :param contract_code:The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param side:    1:Buy Long, 2:Sell Short, 3:Buy to Close Short, 4:Sell to Close Long    (mandatory)
        :param order_quantity:  Order Quantity  (mandatory)
        :param order_price: integral multiple of tick size. If not filled, it means place a market order (optional)
        :return:
        """
        check_symbol(contract_code)
        check_range(side, 1, 4, "side")
        check_should_not_none(order_quantity, "order_quantity")

        params = {
            "param": {
                "contractCode": contract_code,
                "side": side,
                "orderQuantity": order_quantity,
                "orderPrice": order_price
            }
        }
        from hopex.services.trade.post_create_order import CreateOrderService
        return CreateOrderService(params).request(**self.__kwargs)

    def req_condition_orders(self, contract_code_list: list, task_type_list: list, trig_type_list: list,
                             task_status_list: list, direct: int, side: int, start_time: int, end_time: int,
                             page: int = 1, limit: int = 10):
        """
        Query conditoin orders
        :param contract_code_list:  Contract List, Being blank to search all contracts  (optional)
        :param task_type_list:  1:Buy Long, 2:Sell Short, 3:Buy to Close Short, 4:Sell to Close Long,
                                Being blank to search all     (optional)
        :param trig_type_list:  1:Market Price 2:Faire Price,Being blank to search all    (optional)
        :param task_status_list: 1: Untriggered 2.Canceled 3.Order Submitted
                                4.Trigger failed, Being blank to search all       (optional)
        :param direct:  1: LONG, 2: SHORT, 0: Search All      (optional)
        :param side:     1: Sell,2: Buy, 0: Search All        (optional)
        :param start_time:  0:Search All, data from start_time, timestamps(unit microsecond)      (optional)
        :param end_time: 0:Search All, data util end_time, timestamps(unit microsecond)       (optional)
        :param page:  page index
        :param limit:   page limit
        :return:The list of condition orders
        """
        check_range(side, 0, 4, "side")
        check_range(direct, 0, 2, "direct")
        check_range(page, 1, 2000, "page")
        check_range(limit, 1, 2000, "limit")

        params = {
            "param": {
                "contractCodeList": contract_code_list,
                "taskTypeList": task_type_list,
                "trigTypeList": trig_type_list,
                "taskStatusList": task_status_list,
                "direct": direct,
                "side": side,
                "startTime": start_time,
                "endTime": end_time
            }
        }

        page_params = {
            'page': page,
            'limit': limit
        }

        from hopex.services.trade.req_condition_orders import QueryConditionOrdersService
        return QueryConditionOrdersService(params, page_params).request(**self.__kwargs)

    def req_history_orders(self, contract_code_list: list, type_list: list, side: int, start_time: int,
                           end_time: int, page: int = 1, limit: int = 10):
        """
        Query history orders
        :param contract_code_list:  Contract List, Being blank to search all contracts  (optional)
        :param type_list:   1.Limit Price to Open 2.Market Price to Open 3.Limit Price to Close 4.Market Price to Close
                        5.Limit Price Close Partially Complete 6.Market Price Close Partially Complete  (optional)
        :param side:    0:no limit 1 for sell, 2 for buy     (optional)
        :param start_time:  0:Search All, data from start_time, timestamps(unit microsecond)      (optional)
        :param end_time:    0:Search All, data util end_time, timestamps(unit microsecond)       (optional)
        :param page:    page index
        :param limit:      page limit
        :return:The list of history orders
        """
        check_range(side, 0, 4, "side")
        check_range(page, 1, 2000, "page")
        check_range(limit, 1, 2000, "limit")

        params = {
            "param": {
                "contractCodeList": contract_code_list,
                "typeList": type_list,
                "side": side,
                "startTime": start_time,
                "endTime": end_time
            }
        }

        page_params = {
            'page': page,
            'limit': limit
        }

        from hopex.services.trade.req_history_orders import QueryHistoryOrdersService
        return QueryHistoryOrdersService(params, page_params).request(**self.__kwargs)

    def req_liquidation_history(self, contract_code_list: list, side: int, page: int = 1, limit: int = 10):
        """
        Query liquidation history
        :param contract_code_list:  Contract List, leave it black to search all contracts   (optional)
        :param side:0:no limit 1 for sell, 2 for buy    (optional)
        :param page:    page index
        :param limit:    page limit
        :return:The list of liquidation history
        """
        check_range(side, 0, 2, "side")
        check_range(page, 1, 2000, "page")
        check_range(limit, 1, 2000, "limit")
        params = {
            "param": {
                "contractCodeList": contract_code_list,
                "side": side
            }
        }

        page_params = {
            'page': page,
            'limit': limit
        }

        from hopex.services.trade.req_liquidation_history import QueryLiquidationHistoryService
        return QueryLiquidationHistoryService(params, page_params).request(**self.__kwargs)

    def req_order_paras(self, contract_code: str):
        """
        Query order paras
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :return: The object of order paras
        """
        check_symbol(contract_code)
        params = {
            "param": {
                "contractCode": contract_code
            }
        }
        from hopex.services.trade.req_order_paras import QueryOrderParasService
        return QueryOrderParasService(params).request(**self.__kwargs)

    def set_leverage(self, contract_code: str, direct: int, leverage: float):
        """
        Set leverage
        :param contract_code: The contract_code like 'BTCUSDT', 'ETHUSDT', 'LTCUSDT' ... (mandatory)
        :param direct: 1 Long,2 Short   (mandatory)
        :param leverage:    Leverage 1.00~100.00    (mandatory)
        :return:
        """
        check_symbol(contract_code)
        check_should_not_none(direct, "direct")
        check_range(leverage, 1.00, 100.00, "leverage")

        params = {
            'contractCode': contract_code,
            'direct': direct,
            'leverage': leverage
        }
        from hopex.services.trade.post_set_leverage import PostSetLeverageService
        return PostSetLeverageService(params).request(**self.__kwargs)
