from hopex.utils.input_checker import *


class WalletClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs:The option of request connection.
           api_key: The public key applied from Hopex.
           secret_key: The private key applied from Hopex.
           url: The URL name like "https://api2.hopex.com".
           init_log: to init logger
        """
        self.__kwargs = kwargs

    def get_deposit_withdraw(self, page: int = 1, limit: int = 10) -> list:
        """
        Get User Deposit/Withdraw Records
        :param page:page index
        :param limit: page limit
        :return: The list of user deposit/withdraw
        """
        check_range(page, 1, 2000, "page")
        check_range(limit, 1, 2000, "limit")

        params = {
            "page": page,
            "limit": limit
        }

        from hopex.services.wallet.get_deposit_withdraw import GetDepositWithdrawService
        return GetDepositWithdrawService(params).request(**self.__kwargs)

    def get_user_wallet(self):
        """
        Get User Wallet
        :return: The Object of user wallet
        """
        params = {}

        from hopex.services.wallet.get_user_wallet import GetUserWalletService
        return GetUserWalletService(params).request(**self.__kwargs)
