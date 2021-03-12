from home import HomeClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

home_client = HomeClient()

obj = home_client.get_index_statistics()

LogInfo.output(obj)
