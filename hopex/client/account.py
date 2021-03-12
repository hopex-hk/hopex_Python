class AccountClient(object):

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

    def get_user_info(self):
        """
        Get user wealth info
        :return:The object of user wealth info
        """
        params = {}
        from hopex.services.account.get_user_info import GetUserInfoService
        return GetUserInfoService(params).request(**self.__kwargs)
