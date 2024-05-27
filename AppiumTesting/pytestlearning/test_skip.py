import random

import pytest


def test_skipit():
    name = "Rahul1"
    if name == "Rahul":
        pytest.skip('Skipping as name is Rahul')
