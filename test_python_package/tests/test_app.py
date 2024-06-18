import sys

sys.path.append("/home/mshahbazi/test_python_package")

from src.app import add


def test_add():
    assert add(2, 3) == 5
