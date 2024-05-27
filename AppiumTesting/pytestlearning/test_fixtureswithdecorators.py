import pytest


@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")

    yield
    print("Closing DB Connection")


@pytest.fixture(scope='function')
def before():
    print("Launching browser")

    yield
    print("Closing browser")


# def test_dologin(setup,before):
#     print("Executing login test")
#
#
# def test_user_reg(setup,before):
#     print("Executing User Reg test")

@pytest.mark.usefixtures("setup", "before")
def test_dologin():
    print("Executing login test")


@pytest.mark.usefixtures("setup", "before")
def test_user_reg():
    print("Executing User Reg test")
