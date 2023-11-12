import os

import pytest
from datetime import datetime

from src.decorators import log


@pytest.mark.parametrize('arg1, arg2, expected_result', [(1, 2, ' my_function ok'),
                                                         (1, 0,
                                                          ' my_function error: division by zero. Inputs: (1, 0), {}')])
def test_log_decorator_file(arg1, arg2, expected_result):
    filename = 'test.txt'
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def my_function(x, y):
        return x / y

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    my_function(arg1, arg2)
    expected_log = now + expected_result
    with open(filename) as file:
        log_message = file.read().strip()
    assert log_message == expected_log


@pytest.mark.parametrize('arg1, arg2, expected_result', [(1, 2, ' my_function ok'),
                                                         (1, 0,
                                                          ' my_function error: division by zero. Inputs: (1, 0), {}')])
def test_log_decorator_console(capsys, arg1, arg2, expected_result):
    @log()
    def my_function(x, y):
        return x / y

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    my_function(arg1, arg2)
    expected_log = now + expected_result
    log_message = capsys.readouterr()
    assert log_message.out.strip() == expected_log
