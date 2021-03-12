from hopex.constant.definition import Culture

HOPEX_URL_PRO = "https://devapi2.hopex.com"


class RestApiDefine:
    Url = HOPEX_URL_PRO


class HttpMethod:
    GET = "GET"
    GET_SIGN = "GET_SIGN"
    POST = "POST"
    POST_SIGN = "POST_SIGN"


def get_default_server_url():
    return RestApiDefine.Url


def get_default_culture():
    return Culture.ZH_CN
