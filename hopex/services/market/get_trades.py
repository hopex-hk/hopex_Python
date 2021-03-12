from hopex.connection.restapi_sync_client import RestApiSyncClient, HttpMethod


class GetTradesService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v1/trades"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params)
