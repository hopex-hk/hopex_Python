from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class PostQueryMarketDepthService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v1/depth"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST, channel, self.params)
