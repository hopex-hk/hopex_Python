from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class CreateOrderService:
    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v1/order"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params)
