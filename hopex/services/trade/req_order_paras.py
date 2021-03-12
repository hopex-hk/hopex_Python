from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class QueryOrderParasService:
    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v1/get_orderParas"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params)
