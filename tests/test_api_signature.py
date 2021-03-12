import unittest
import hopex

from unittest import mock
from hopex.utils import *


class TestApi(unittest.TestCase):
    def test_request(self):
        builder = UrlParamsBuilder()
        api_signature.utc_now = mock.Mock(return_value="123")
        create_signature("123", "456", "GET", "/api/v1/userinfo", builder)
        self.assertEqual(
            "hmac apikey=\"123\", algorithm=\"hmac-sha256\", headers=\"date request-line digest\", "
            "signature=\"KlgJ6m3FZYE3rsjdYXOZf4EhvDTJCTPOjxpXFg1thnA=\"",
            builder.header_map.get('Authorization', None))
        # print(builder.header_map.get('Authorization', None))
        return


if __name__ == "__main__":
    unittest.main()
