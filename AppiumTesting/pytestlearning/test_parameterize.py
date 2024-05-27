import logging

import pytest
from utilities.generatingLogs import log

log = Logger(__name__, logging.INFO)


def get_data():
    return [

        ("trainer@way2automation.com", "kjsdfbksdf"),
        ("java@way2automation.com", "sdf"),
        ("info@way2automation.com", "sdfsdf")

    ]



@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
    logger = log()
    logger.info("This is a v new log")
    logger.error("This is an v error message")
