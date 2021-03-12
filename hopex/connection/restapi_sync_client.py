import logging

from hopex.utils.api_signature import create_signature
from hopex.exception.hopex_api_exception import HopexApiException
from hopex.connection.restapi_invoker import call_sync, call_sync_performance_test
from hopex.connection.impl.restapi_request import *
from hopex.constant.system import *
from hopex.utils.url_params_builder import UrlParamsBuilder


class RestApiSyncClient(object):

    def __init__(self, **kwargs):
        """
       Create the request client instance.
       :param kwargs: The option of request connection.
           api_key: The public key applied from Hopex.
           secret_key: The private key applied from Hopex.
           url: The URL name like "https://api2.hopex.com".
           performance_test: for performance test
           init_log: to init logger
       """
        self.__api_key = kwargs.get("api_key", None)
        self.__secret_key = kwargs.get("secret_key", None)
        self.__server_url = kwargs.get("url", get_default_server_url())
        self.__culture = kwargs.get('culture', get_default_culture())
        self.__init_log = kwargs.get("init_log", None)
        self.__performance_test = kwargs.get("performance_test", None)
        if self.__init_log and self.__init_log:
            logger = logging.getLogger("huobi-client")
            logger.setLevel(level=logging.INFO)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(handler)

    def __create_request_by_get(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json', 'User-Agent': 'bcoin'})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, url, builder)
        request.header.update(builder.header_map)
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, url, builder)
        request.header.update(builder.header_map)
        if len(builder.post_list):  # specify for case : /v1/order/batch-orders
            request.post_body = builder.post_list
        else:
            request.post_body = builder.post_map
        request.url = url + builder.build_url()
        return request

    def create_request(self, method, url, params, page):
        builder = UrlParamsBuilder()
        builder.put_url('culture', self.__culture)

        if params and len(params):
            if method in [HttpMethod.GET, HttpMethod.GET_SIGN]:
                for key, value in params.items():
                    builder.put_url(key, value)
            elif method in [HttpMethod.POST, HttpMethod.POST_SIGN]:
                for key, value in params.items():
                    builder.put_post(key, value)
            else:
                raise HopexApiException(HopexApiException.EXEC_ERROR,
                                        "[error] undefined HTTP method")
        if page and len(page):
            for key, value in page.items():
                builder.put_url(key, value)

        if method == HttpMethod.GET:
            request = self.__create_request_by_get(url, builder)
        elif method == HttpMethod.GET_SIGN:
            request = self.__create_request_by_get_with_signature(url, builder)
        elif method == HttpMethod.POST_SIGN:
            request = self.__create_request_by_post_with_signature(url, builder)
        elif method == HttpMethod.POST:
            request = self.__create_request_by_post_with_signature(url, builder)
        else:
            raise HopexApiException(HopexApiException.INPUT_ERROR, "[Input] " + method + "  is invalid http method")

        # request.json_parser = parse
        return request

    def request_process(self, method, url, params, page=None):
        if self.__performance_test is not None and self.__performance_test is True:
            return self.request_process_performance(method, url, params, page)
        else:
            return self.request_process_product(method, url, params, page)

    def request_process_product(self, method, url, params, page):
        request = self.create_request(method, url, params, page)
        if request:
            return call_sync(request)

    def request_process_performance(self, method, url, params, page):
        request = self.create_request(method, url, params, page)
        if request:
            return call_sync_performance_test(request)

        return None, 0, 0
