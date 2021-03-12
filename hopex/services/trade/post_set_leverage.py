from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class PostSetLeverageService:
    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v1/set_leverage"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params)
