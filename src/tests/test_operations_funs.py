from unittest.mock import patch
from unittest import mock

from helper_modules.operations_funcs import append_data

@patch('builtins.input')
@patch('builtins.input')
def test_append_data(mock_input, mock_input2):
    mock_input.return_value = 'time'
    mock_input2.return_value = 1.4
