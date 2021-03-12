from hopex.client.wallet import WalletClient
from hopex.constant.test import t_api_key, t_secret_key
from hopex.utils.log_info import LogInfo

wallet_client = WalletClient(api_key=t_api_key, secret_key=t_secret_key)

obj = wallet_client.get_user_wallet()

LogInfo.output(obj)
