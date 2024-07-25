import pytest

from pytest_req.log import log_cfg


@pytest.fixture(scope="session", autouse=True)
def setup_log():
    """
    setup log
    """
    # setting log level
    # log_cfg.set_level(level="INFO")
    # close log color
    # log_cfg.set_level(colorlog=False)
    # setting log format
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</> |<level> {level} | {message}</level>"
    log_cfg.set_level(format=log_format)
