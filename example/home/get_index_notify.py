from hopex.client.home import HomeClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

home_client = HomeClient()

list_obj = home_client.get_index_notify()

LogInfo.output_list(list_obj)
