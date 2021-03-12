from hopex.utils.input_checker import check_range


class HomeClient(object):

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

    def get_index_statistics(self):
        """
        Get Index Statistics
        :return:The object of index statistics
        """
        params = {}
        from hopex.services.home.get_index_statistics import GetIndexStatisticsService
        return GetIndexStatisticsService(params).request(**self.__kwargs)

    def get_index_notify(self, page: int = 1, limit: int = 5):
        """
        Get Index Notify
        :return:The list of notifies
        """
        check_range(page, 1, 2000, "page")
        check_range(limit, 1, 2000, "limit")
        params = {'page': page, 'limit': limit}
        from hopex.services.home.get_index_notify import GetIndexNotifyService
        return GetIndexNotifyService(params).request(**self.__kwargs)
