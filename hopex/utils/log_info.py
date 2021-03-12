import json


class LogLevel:
    DEBUG = "debug"
    INFO = "info"
    WARNINGS = "warning"
    ERROR = "error"
    FATAL = "fatal"


class LogInfo:
    @staticmethod
    def output(message, name=None, log_level=LogLevel.DEBUG):
        # if (message and len(message)):
        #     if log_level == LogLevel.DEBUG:
        #         logging.debug(message)
        #     elif log_level == LogLevel.INFO:
        #         logging.info(message)
        #     elif log_level == LogLevel.WARNINGS:
        #         logging.warnings(message)
        #     elif log_level == LogLevel.ERROR:
        #         logging.error(message)
        #     elif log_level == LogLevel.FATAL:
        #         logging.fatal(message)
        if name:
            print(name)
        if message and len(message):
            print(json.dumps(message, indent=4, ensure_ascii=False) + '\n')
        else:
            print()

    @staticmethod
    def output_list(data_list, name=None, log_level=LogLevel.DEBUG):
        if name:
            print(name)
        if data_list and len(data_list):
            print(json.dumps(data_list, indent=4, ensure_ascii=False) + '\n')
        else:
            print()
