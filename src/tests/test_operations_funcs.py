from unittest.mock import patch

from helper_modules.menu_operations import main_menu

@patch('builtins.input')
def test_main_menu(mock_input):
    # Product selection
    mock_input.return_value = '1'
    expected = ['1', 'product']
    actual1, actual2 = main_menu()

    assert actual1 == expected[0]
    assert actual2 == expected[1]

    # Courier selection
    mock_input.return_value = '2'
    expected = ['2', 'courier']
    actual1, actual2 = main_menu()

    assert actual1 == expected[0]
    assert actual2 == expected[1]

    # Orders selection
    mock_input.return_value = '3'
    expected = ['3', 'orders']
    actual1, actual2 = main_menu()

    assert actual1 == expected[0]
    assert actual2 == expected[1]

    # None selection