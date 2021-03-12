from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class QueryConditionOrdersService:
    def __init__(self, params, page_params):
        self.params = params
        self.page_params = page_params

    def request(self, **kwargs):
        channel = "/api/v1/condition_order_info"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, self.page_params)
