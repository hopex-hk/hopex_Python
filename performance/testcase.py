import time

from hopex.client.account import AccountClient
from hopex.constant.definition import CandlestickInterval, OrderType, OrderTradeType, Direct
from hopex.client.home import HomeClient
from hopex.client.market import MarketClient
from hopex.client.trade import TradeClient
from hopex.client.wallet import WalletClient
from hopex.constant.test import t_api_key, t_secret_key

ROUND_SIZE = 3
count_offset = 0
time_cost_detail_list = []

# prepare list
contract_code = 'BTCUSDT'


class RunStatus:
    SUCCESS = "OK"
    FAILED = "Fail"


class TimeCost:
    sdk_api_start_time = 0.0  # SDK call start time
    server_req_cost = 0.0  # time cost from response.elapsed.total_seconds(), cost is from sending request to receive response
    server_api_cost = 0.0  # manually statistics time before/after requests.get  (server_api_cost >= server_req_cost)
    function_name = ""
    run_status = ""

    def __init__(self, function_name=""):
        self.sdk_api_start_time = round(time.time(), ROUND_SIZE + 1)
        self.function_name = function_name

    def add_record(self):
        sdk_api_end_time = round(time.time(), ROUND_SIZE + 1)
        sdk_api_cost = sdk_api_end_time - self.sdk_api_start_time
        sdk_cost_req = sdk_api_cost - self.server_req_cost
        sdk_cost_manual = sdk_api_cost - self.server_api_cost

        row_dict = {
            "sdk_api_cost": round(sdk_api_cost, ROUND_SIZE),
            "server_api_cost": round(self.server_api_cost, ROUND_SIZE + 1),
            "server_req_cost": round(self.server_req_cost, ROUND_SIZE + 1),
            "sdk_api_delay": round(sdk_cost_manual, ROUND_SIZE),
            "sdk_req_delay": round(sdk_cost_req, ROUND_SIZE),
            "sdk_func_name": self.function_name,
            "run_status": self.run_status,
            "sdk_test_start_time": self.sdk_api_start_time
        }
        global time_cost_detail_list
        time_cost_detail_list.append(row_dict)

    @staticmethod
    def output_sdk_cost_list(data_list, format_str="", only_brief=False):
        TimeCost.output_sdk_header(format_str, only_brief)

        for dict_data in data_list:
            TimeCost.output_sdk_cost(dict_data, format_str, only_brief)

    @staticmethod
    def output_sdk_header(format_str, only_brief):
        delay_server_api_cost = "delay(server_api_cost){format_str}".format(format_str=format_str)
        delay_server_req_cost = "delay(server_req_cost){format_str}".format(format_str=format_str)
        sdk_api_cost = "sdk_api_cost{format_str}".format(format_str=format_str)

        sdk_test_start_time = "sdk_test_start_time{format_str}".format(format_str=format_str)
        sdk_func_name = "sdk_func_name{format_str}".format(format_str=format_str)
        run_status = "run_status{format_str}".format(format_str=format_str)

        if only_brief:
            print(delay_server_api_cost,
                  delay_server_req_cost,
                  sdk_api_cost)
        else:
            print(
                delay_server_api_cost,
                delay_server_req_cost,
                sdk_api_cost,
                sdk_test_start_time,
                sdk_func_name,
                run_status)

    @staticmethod
    def output_sdk_cost(dict_data, format_str, only_brief):
        sdk_test_start_time = dict_data.get("sdk_test_start_time", "")
        if sdk_test_start_time:
            sdk_test_start_time_desc = "{sdk_test_start_time}{format_str}".format(
                sdk_test_start_time=dict_data["sdk_test_start_time"],
                format_str=format_str)
        else:
            sdk_test_start_time_desc = ""

        sdk_api_delay_desc = "{sdk_api_delay}({server_api_cost}){format_str}".format(
            sdk_api_delay=dict_data["sdk_api_delay"],
            server_api_cost=dict_data["server_api_cost"],
            format_str=format_str)

        sdk_req_delay_desc = "{sdk_req_delay}({server_req_cost}){format_str}".format(
            sdk_req_delay=dict_data["sdk_req_delay"],
            server_req_cost=dict_data["server_req_cost"],
            format_str=format_str)

        sdk_api_cost_desc = "{sdk_api_cost}{format_str}".format(
            sdk_api_cost=dict_data["sdk_api_cost"],
            format_str=format_str)

        sdk_func_name = dict_data.get("sdk_func_name", None)
        if sdk_func_name:
            sdk_func_name_desc = "{sdk_func_name}{format_str}".format(
                sdk_func_name=dict_data["sdk_func_name"],
                format_str=format_str)
        else:
            sdk_func_name_desc = ""

        run_status = dict_data.get("run_status", None)
        if run_status:
            run_status_desc = "{run_status}{format_str}".format(
                run_status=dict_data["run_status"],
                format_str=format_str)
        else:
            run_status_desc = ""

        if only_brief:
            print(
                sdk_api_delay_desc,
                sdk_req_delay_desc,
                sdk_api_cost_desc,
            )
        else:
            print(
                sdk_api_delay_desc,
                sdk_req_delay_desc,
                sdk_api_cost_desc,
                sdk_test_start_time_desc,
                sdk_func_name_desc,
                run_status_desc
            )

    @staticmethod
    def output_sort_cost(by_key_name, is_sorted=False):
        global time_cost_detail_list

        if is_sorted:
            output_list = sorted(time_cost_detail_list, key=lambda e: e.__getitem__(by_key_name), reverse=True)
        else:
            output_list = time_cost_detail_list

        TimeCost.output_sdk_cost_list(data_list=output_list, format_str="\t", only_brief=False)

    @staticmethod
    def output_average_cost():
        global time_cost_detail_list
        global count_offset
        sum_final = {}
        average_final = {}
        average_count = 0
        sum_key_list = ["sdk_api_cost", "server_api_cost", "server_req_cost", "sdk_api_delay", "sdk_req_delay"]
        if len(time_cost_detail_list):
            average_count = len(time_cost_detail_list) + count_offset
            for key_name in sum_key_list:
                sum_final[key_name] = sum(row[key_name] for row in time_cost_detail_list)
                average_final[key_name] = round(sum_final[key_name] / average_count, ROUND_SIZE)

        print("api counts :", average_count, count_offset)
        # TimeCost.output_sdk_cost_list(data_list=[sum_final], only_brief=True)
        TimeCost.output_sdk_cost_list(data_list=[average_final], only_brief=True)


class RestfulTestCaseSeq:
    def __init__(self):
        pass

    def test_account(self):
        account_client = AccountClient(api_key=t_api_key, secret_key=t_secret_key, performance_test=True)

        # case get_user_info
        tc = TimeCost(function_name=account_client.get_user_info.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_user_info()
        print("get_user_info:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_home(self):
        home_client = HomeClient(api_key=t_api_key, secret_key=t_secret_key, performance_test=True)
        # case get_index_notify
        tc = TimeCost(function_name=home_client.get_index_notify.__name__)
        result, tc.server_req_cost, tc.server_api_cost = home_client.get_index_notify()
        print("get_index_notify:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_index_statistics
        tc = TimeCost(function_name=home_client.get_index_statistics.__name__)
        result, tc.server_req_cost, tc.server_api_cost = home_client.get_index_statistics()
        print("get_index_statistics:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_market(self):
        market_client = MarketClient(api_key=t_api_key, secret_key=t_secret_key, performance_test=True)

        # case get_kline
        tc = TimeCost(function_name=market_client.get_kline.__name__)
        end_time = int(time.time())
        start_time = end_time - 60 * 60 * 24

        result, tc.server_req_cost, tc.server_api_cost = market_client.get_kline(contract_code, end_time, start_time,
                                                                                 CandlestickInterval.MIN5)
        print("get_kline:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_markets
        tc = TimeCost(function_name=market_client.get_markets.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_markets()
        print("get_markets:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_market_ticker
        tc = TimeCost(function_name=market_client.get_market_ticker.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_market_ticker(contract_code)
        print("get_market_ticker:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_trades
        tc = TimeCost(function_name=market_client.get_trades.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_trades(contract_code)
        print("get_trades:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case post_query_market_depth
        tc = TimeCost(function_name=market_client.post_query_market_depth.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.post_query_market_depth(contract_code)
        print("post_query_market_depth:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_trade(self):
        trade_client = TradeClient(api_key=t_api_key, secret_key=t_secret_key, performance_test=True)

        # case req_order_paras
        tc = TimeCost(function_name=trade_client.req_order_paras.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.req_order_paras(contract_code)
        print("req_order_paras:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case req_liquidation_history
        tc = TimeCost(function_name=trade_client.req_liquidation_history.__name__)
        contract_code_list = [contract_code]
        side = 0
        result, tc.server_req_cost, tc.server_api_cost = trade_client.req_liquidation_history(contract_code_list,
                                                                                              side)
        print("req_liquidation_history:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case req_history_orders
        tc = TimeCost(function_name=trade_client.req_history_orders.__name__)
        contract_code_list = list()
        type_list = list()
        side = 0
        start_time = 0
        end_time = 0

        result, tc.server_req_cost, tc.server_api_cost = trade_client.req_history_orders(contract_code_list,
                                                                                         type_list, side, start_time,
                                                                                         end_time)
        print("req_history_orders:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_positions
        tc = TimeCost(function_name=trade_client.get_positions.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.get_positions()
        print("get_positions:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_open_orders
        tc = TimeCost(function_name=trade_client.get_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.get_open_orders(contract_code)
        print("get_open_orders:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case set_leverage
        tc = TimeCost(function_name=trade_client.set_leverage.__name__)
        direct = Direct.LONG
        leverage = 20
        result, tc.server_req_cost, tc.server_api_cost = trade_client.set_leverage(contract_code, direct, leverage)
        print("set_leverage:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case create_order
        tc = TimeCost(function_name=trade_client.create_order.__name__)
        side = OrderTradeType.BUY_LONG
        order_quantity = 10
        order_price = 48000
        result, tc.server_req_cost, tc.server_api_cost = trade_client.create_order(contract_code, side, order_quantity,
                                                                                   order_price)
        print("create_order:", result)
        order_id_tmp = result['data'] if result and result.get('ret', -1) == 0 else 0
        tc.run_status = RunStatus.SUCCESS if result and result.get('ret', -1) == 0 else RunStatus.FAILED
        tc.add_record()

        # case cancel_order
        tc = TimeCost(function_name=trade_client.cancel_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.cancel_order(contract_code, order_id_tmp)
        print("cancel_order:", result)
        tc.run_status = RunStatus.SUCCESS if result and result.get('ret', -1) == 0 else RunStatus.FAILED
        tc.add_record()

        # case create_condition_order
        tc = TimeCost(function_name=trade_client.create_condition_order.__name__)
        side = OrderTradeType.BUY_LONG
        trig_price = 50000
        expected_quantity = 10
        expected_price = 48000
        result, tc.server_req_cost, tc.server_api_cost = trade_client.create_condition_order(contract_code, side,
                                                                                             OrderType.LIMIT,
                                                                                             trig_price,
                                                                                             expected_quantity,
                                                                                             expected_price)
        print("create_condition_order:", result)
        tc.run_status = RunStatus.SUCCESS if result and result.get('ret', -1) == 0 else RunStatus.FAILED
        tc.add_record()

        # case req_condition_orders
        tc = TimeCost(function_name=trade_client.req_condition_orders.__name__)
        contract_code_list = [contract_code]
        task_type_list = list()
        trig_type_list = list()
        task_status_list = list()
        direct = 0
        side = 0
        start_time = 0
        end_time = 0
        result, tc.server_req_cost, tc.server_api_cost = trade_client.req_condition_orders(contract_code_list,
                                                                                           task_type_list,
                                                                                           trig_type_list,
                                                                                           task_status_list, direct,
                                                                                           side, start_time, end_time)
        print("req_condition_orders:", result)
        task_data = result.get('data', {}) if result and result.get('ret', -1) == 0 else {}
        task_list = task_data.get('result', list())

        task_list = list(filter(lambda x: x['taskStatus'] == 1 if x.get('taskStatus') else False, task_list))
        print(task_list)
        task_id_tmp = task_list[0].get('taskId', 0) if len(task_list) else 0

        tc.run_status = RunStatus.SUCCESS if result and result.get('ret', -1) == 0 else RunStatus.FAILED
        tc.add_record()

        # case cancel_condition_order
        tc = TimeCost(function_name=trade_client.cancel_condition_order.__name__)
        print(task_id_tmp)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.cancel_condition_order(contract_code, task_id_tmp)
        print("cancel_condition_order:", result)
        tc.run_status = RunStatus.SUCCESS if result and result.get('ret', -1) == 0 else RunStatus.FAILED
        tc.add_record()

    def test_wallet(self):
        wallet_client = WalletClient(api_key=t_api_key, secret_key=t_secret_key, performance_test=True)

        # case get_user_wallet
        tc = TimeCost(function_name=wallet_client.get_user_wallet.__name__)
        result, tc.server_req_cost, tc.server_api_cost = wallet_client.get_user_wallet()
        print("get_user_wallet:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_deposit_withdraw
        tc = TimeCost(function_name=wallet_client.get_deposit_withdraw.__name__)
        result, tc.server_req_cost, tc.server_api_cost = wallet_client.get_deposit_withdraw()
        print("get_deposit_withdraw:", result)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()


if __name__ == "__main__":
    test_case = RestfulTestCaseSeq()
    # test_case.test_account()
    test_case.test_home()
    test_case.test_market()
    # test_case.test_trade()
    # test_case.test_wallet()

    print("\n\n==================api execute sequence=========================")
    TimeCost.output_sort_cost(by_key_name="", is_sorted=False)

    print("\n\n======================order by api delay time desc=====================")
    TimeCost.output_sort_cost(by_key_name="sdk_api_delay", is_sorted=True)

    print("\n\n======================average cost/delay time=====================")
    TimeCost.output_average_cost()
