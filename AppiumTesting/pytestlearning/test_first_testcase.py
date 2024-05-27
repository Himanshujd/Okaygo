import pytest


def setup_module(module):
    print("Creating DB Connection")


def teardown_module(module):
    print("Closing DB Connection")


def setup_function(function):
    print("launching browser")


def teardown_function(function):
    print("Quitting the browser")


def test_dologin():
    print("Executing login test")


def test_user_reg():
    print("Executing User Reg test")
