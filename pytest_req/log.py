"""
pytest-req log
"""
import inspect
import os
import sys

from loguru import logger

from pytest_req.config import Config

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
exec_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(exec_dir, "logs")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

with open(os.path.join(report_dir, "requests_log.log"), "w") as log:
    log.truncate(0)

if Config.LOG_PATH is None:
    Config.LOG_PATH = os.path.join(report_dir, "requests_log.log")


class LogConfig:
    """log config"""

    def __init__(self, level: str = "DEBUG", colorlog: bool = True):
        self.logger = logger
        self._colorlog = colorlog
        self._console_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</> <level>| {level: <8} | {file} | {message}</level>"
        self._log_format = "{time: YYYY-MM-DD HH:mm:ss} | <level>{level: <8}</level> | {file: <10} | {message}"
        self._level = level
        self.logfile = Config.LOG_PATH
        self.set_level(self._colorlog, self._console_format, self._level)

    def set_level(self, colorlog: bool = True, format: str = None, level: str = "DEBUG"):
        """
        setting level
        :param colorlog:
        :param format:
        :param level:
        :return:
        """
        if format is None:
            format = self._console_format
        self.logger.remove()
        self._level = level
        self.logger.add(sys.stderr, level=level, colorize=colorlog, format=format)
        self.logger.add(self.logfile, level=level, colorize=False, format=self._log_format, encoding="utf-8")


# log level: TRACE < DEBUG < INFO < SUCCESS < WARNING < ERROR
log_cfg = LogConfig(level="TRACE")
log = logger
