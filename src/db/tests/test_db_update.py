from unittest import mock
import pytest

from unittest.mock import patch
from db.setup_db import HelperDB, add_to_db, update_to_db

class Test_Update_Product:
    ### Update Product, but only change price ###
    @patch("builtins.input", side_effect=['11', 'Sausage Rolls', 2.2])
    @patch("builtins.print")
    def test_update_to_db_product_change_price(self, mock_print, mock_input):

        mock_input
        update_to_db('product', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM product WHERE name = "Sausage Rolls"')[0]
        assert 'Sausage Rolls' and 2.2 in actual
        # Reset changes
        db.execute_operation('UPDATE product SET price = 1.2 WHERE id = 11;')

    ### Update Product, but only change Name ###
    @patch("builtins.input", side_effect=['11', 'Chicken Rolls', 1.2])
    @patch("builtins.print")
    def test_update_to_db_product_change_name(self, mock_print, mock_input):

        mock_input
        update_to_db('product', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM product WHERE name = "Chicken Rolls"')[0]
        assert 'Chicken Rolls' in actual
        # Reset changes
        db.execute_operation('UPDATE product SET name = "Sausage Rolls" WHERE id = 11;')
    
    ### Update Product, change name and price ###
    @patch("builtins.input", side_effect=['11', 'Hot Dog', 3.2])
    @patch("builtins.print")
    def test_update_to_db_product_change_both(self, mock_print, mock_input):

        mock_input
        update_to_db('product', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM product WHERE id = 11')[0]
        assert 'Hot Dog' and 3.2 in actual
        # Reset changes
        db.execute_operation('UPDATE product SET name = "Sausage Rolls", price = 1.2 WHERE id = "11";')
    
    ### Update Product, no change  ###
    @patch("builtins.input", side_effect=['11', '', ''])
    @patch("builtins.print")
    def test_update_to_db_product_no_change(self, mock_print, mock_input):
        mock_input
        update_to_db('product', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM product WHERE id = 11')[0]
        assert 'Sausage Rolls' and 1.2 in actual

class Test_Update_Courier:
    ### Update Courier, but only change name ###
    @patch("builtins.input", side_effect=['2', 'Leo', '07888383812'])
    @patch("builtins.print")
    def test_update_to_db_courier_name_change(self, mock_print, mock_input):

        mock_input
        update_to_db('courier', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM courier WHERE id = 2')[0]
        assert 'Leo' in actual
        # Reset changes
        db.execute_operation('UPDATE courier SET name = "LL" WHERE id = 2;')

    ### Update Courier, but only change phone number ###
    @patch("builtins.input", side_effect=['2', 'LL', '07883819385'])
    @patch("builtins.print")
    def test_update_to_db_courier_change_phone(self, mock_print, mock_input):

        mock_input
        update_to_db('courier', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM courier WHERE id = 2')[0]
        assert '07883819385' in actual
        # Reset changes
        db.execute_operation('UPDATE courier SET phone = "07888383812" WHERE id = 2;')
    
    ### Update Courier, change name and phone ###
    @patch("builtins.input", side_effect=['2', 'Leo', '07883819385'])
    @patch("builtins.print")
    def test_update_to_db_courier_change_both(self, mock_print, mock_input):

        mock_input
        update_to_db('courier', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM courier WHERE id = 2')[0]
        assert 'Leo' and '07883819385' in actual
        # Reset changes
        db.execute_operation('UPDATE courier SET name = "LL", phone = "07888383812" WHERE id = 2;')
    
    ### Update Product, no change  ###
    @patch("builtins.input", side_effect=['2', '', ''])
    @patch("builtins.print")
    def test_update_to_db_product_no_change(self, mock_print, mock_input):
        mock_input
        update_to_db('courier', test=True)
        
        ## Check if data has gone through database execution
        mock_print.assert_called_with("\nData has been updated!\n")
        assert mock_input.call_count == 3
        
        ## Check if the data has been changed
        db = HelperDB(test=True)
        actual = db.fetch_all(f'SELECT * FROM courier WHERE id = 2')[0]
        assert 'LL' and '07888383812' in actual

class Test_Update_Order_Status:
    ### Update Order status###
    @patch("builtins.input", side_effect=['1', '2'])
    def test_update_to_db_order_status(self, mock_input):
        mock_input
        add_to_db('orders', ['Miles', '99th Street', '07352114852', 1, 1, [1,2]], test=True)
        update_to_db('update_order_status', test=True)

        assert mock_input.call_count == 2
        db = HelperDB(test=True)
        actual = db.fetch_all(f"SELECT * FROM orders" 
                + " INNER JOIN customer_detail"
                + " ON orders.customer_detail_id = customer_detail_id"
                + " WHERE customer_name = 'Miles';", dict_cur=True)
        actual_status = db.fetch_all(f'SELECT * FROM orders WHERE id = 1')
        # Check customer detail addition check
        assert 'Miles' and '99th Street' in actual[0].values()
        assert 2 in actual_status[0]

        db.execute_operation('TRUNCATE orders')
        db.execute_operation('DELETE FROM customer_detail WHERE customer_name = "Miles"')