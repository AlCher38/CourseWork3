import pytest
from src.utils import *


def test_get_executed_operations():
    assert get_executed_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
