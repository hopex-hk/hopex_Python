class Culture:
    ZH_CN = 'zh-CN'
    EN = 'en'
    EN_US = 'en'
    ZH_HK = 'zh-HK'
    JA_JP = 'ja-JP'
    KO_KR = 'ko-KR'


class CandlestickInterval:
    MIN1 = "1m"
    MIN5 = "5m"
    HOUR1 = "1h"
    DAY1 = "1d"
    MON1 = "1M"
    WEEK1 = "1w"
    INVALID = None


class OrderType:
    LIMIT = "Limit"
    MARKET = "Market"
    INVALID = None


class OrderSide:
    SELL = 1
    BUY = 2
    INVALID = None


class OrderTradeType:
    BUY_LONG = 1
    SELL_SHORT = 2
    BUY_TO_CLOSE_SHORT = 3
    SELL_TO_CLOSE_LONG = 4


class Direct:
    LONG = 1
    SHORT = 2
