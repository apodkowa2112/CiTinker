import sys


def test_running_in_virtual_environment():
    assert sys.prefix != sys.base_prefix