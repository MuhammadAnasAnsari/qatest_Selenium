# In the command line / terminal we use "-v -rxs" in  directory>"pytest -v -rxs test_demo_skip.py" to see the reason of skipped.
# Use "-k" to run the test [with any part of its] function_name in  directory>"pytest -v -rxs -k demo"

import pytest    # import the pytest lib to implement pytest functionalities like fixtures yield, mark.skip
import sys



@pytest.mark.windows
def test_windows_1():             # To get windows function directory>pytest test_demo_skip.py -m windows -v
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True
# @pytest.mark.skip(reason="Not included in this build!")
# def test_demo_1():
#     assert True
#
# @pytest.mark.skipif(sys.version_info < (3,8),
#                     reason='requires Python 3.8 or higher')
#
# def test_demo_2():
#     assert True
#
# def test_demo_3():
#     assert True