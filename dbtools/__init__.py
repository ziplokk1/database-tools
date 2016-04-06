"""
Prerequisites:
  libmyodbc
  unixodbc-bin
  unixodbc-dev

  sudo apt-get install libmyodbc unixodbc-bin unixodbc-dev
"""

import pyodbc
import logging
import time


logger = logging.getLogger('dbtools')
retry_timeout = 30


class DatabaseConnection(object):
    """
    Context manager for odbc database connections.
    """

    def __init__(self, connection_string):
        self.database = pyodbc.connect(connection_string)
        self.cursor = self.database.cursor()

    def close(self):
        self.cursor.close()
        self.database.close()

    def __enter__(self):
        """
        :rtype: pyodbc.Cursor
        :return:
        """
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return bool(exc_type)


def _retry_on_lock(f):
    """
    Continue to retry transaction while "lock" is in the error message.

    This should include deadlocks and lock wait timeouts.
    :param f: function to wrap

    :return:
    """
    def inner(*args, **kwargs):
        for i in range(5):
            try:
                return f(*args, **kwargs)
            except pyodbc.Error as e1:
                logger.error(e1)
                if 'lock' in e1.args[1].lower():
                    time.sleep(retry_timeout)
                    continue
                raise
        else:
            raise Exception('max retries exceeded when attempting to write to database.')
    return inner
