from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class CreateConditionOrderService:
    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v1/condition_order"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params)
