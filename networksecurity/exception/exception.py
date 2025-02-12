import sys
from networksecurity.logging.logger import logging
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _, exc_table = error_details.exc_info()
        self.lineno = exc_table.tb_lineno
        self.file_name = exc_table.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python scripe name [{0}] line number [{1} error message [{2}]]".format(self.file_name, self.lineno, self.error_message)
