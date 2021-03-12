import re
import time

from hopex.exception.hopex_api_exception import HopexApiException

reg_ex = "[ _`~!@#$%^&*()+=|{}':;',\\[\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“’。，、？]|\n|\t"


def check_symbol(symbol):
    if not isinstance(symbol, str):
        raise HopexApiException(HopexApiException.INPUT_ERROR, "[Input] symbol must be string")
    if re.match(reg_ex, symbol):
        raise HopexApiException(HopexApiException.INPUT_ERROR, "[Input] " + symbol + "  is invalid symbol")


def check_symbol_list(symbols):
    if not isinstance(symbols, list):
        raise HopexApiException(HopexApiException.INPUT_ERROR, "[Input] symbols in subscription is not a list")
    for symbol in symbols:
        check_symbol(symbol)


def check_range(value, min_value, max_value, name):
    if value is None:
        return
    if min_value > value or value > max_value:
        raise HopexApiException(HopexApiException.INPUT_ERROR,
                                "[Input] " + name + " is out of bound. " + str(value) + " is not in [" + str(
                                    min_value) + "," + str(max_value) + "]")


def check_should_not_none(value, name):
    if value is None:
        raise HopexApiException(HopexApiException.INPUT_ERROR, "[Input] " + name + " should not be null")


def check_should_none(value, name):
    if value is not None:
        raise HopexApiException(HopexApiException.INPUT_ERROR, "[Input] " + name + " should be null")


def check_in_list(value, list_configed, name):
    if (value is not None) and (value not in list_configed):
        raise HopexApiException(HopexApiException.INPUT_ERROR,
                                "[Input] " + name + " should be one in " + (",".join(list_configed)))


