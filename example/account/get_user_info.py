from hopex.client.account import AccountClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

account_client = AccountClient(api_key=t_api_key, secret_key=t_secret_key)

obj = account_client.get_user_info()

LogInfo.output(obj)
