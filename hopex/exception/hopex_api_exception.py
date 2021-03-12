class HopexApiException(Exception):

    INPUT_ERROR = "InputError"
    KEY_MISSING = "KeyMissing"
    EXEC_ERROR = "ExecuteError"

    def __init__(self, err_code, err_message):
        self.err_code = err_code
        self.err_message = err_message
