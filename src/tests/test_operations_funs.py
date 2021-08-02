from unittest.mock import patch
from unittest import mock

from helper_modules.operations_funcs import append_data, extra_order_info

@patch('builtins.input')
@patch('builtins.input')
def test_append_data(mock_input, mock_input2):
    mock_input.return_value = 'time'
    mock_input2.return_value = 1.4
    pass

@patch('builtins.input', side_effect=['Miles', '99th Street', '07352114852', '1,2', 1])
def test_extra_order_info(mock_input):
    expected = ['Miles', '99th Street', '07352114852', 1, 1, [1,2]]
    actual = extra_order_info('product', 'courier')
    
    mock_input.call_count = 5
    assert actual == expected