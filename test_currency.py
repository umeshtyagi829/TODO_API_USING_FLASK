import unittest
from currency import Currency
import json 

class Testcurrency(unittest.TestCase):
    
    def setUp(self):
        self.currency = Currency()

    def test_list_currencies(self):
        result = self.currency.list_currencies()
        self.assertEqual(result.status_code, 200)

    def test_currency_value_in_others(self):
        result = self.currency.currency_value_in_others(country_code='inr')
        self.assertEqual(result.status_code, 200)
        
    def test_get_exchange_rate(self):
        result = self.currency.get_exchange_rate(base_currency_code='usd', target_currency_code='inr')
        self.assertEqual(result.status_code, 200)
        
    def test_currency_value_in_others_with_invalid_value(self):
        result = self.currency.currency_value_in_others(country_code='iprr')
        self.assertEqual(result.status_code, 403)
        
    def test_get_exchange_rate_with_invalid_value(self):
        result = self.currency.get_exchange_rate(base_currency_code='urtd', target_currency_code='inr')
        self.assertEqual(result.status_code, 403)
        

if __name__ == '__main__':
    unittest.main()