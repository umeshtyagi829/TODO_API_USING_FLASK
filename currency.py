from utils import get_response
import json
import argparse
from prettytable import PrettyTable

class Currency():
    def __init__(self):
        self.base_url  = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest"
    
    def list_currencies(self):
        """Lists all the available currencies in prettified json format"""
        url = f'{self.base_url}/currencies.json'
        return get_response(url)

    def currency_value_in_others(self, country_code):
        """Get the currency list with any as base currency"""
        url = f'{self.base_url}/currencies/{country_code.lower()}.json'
        return get_response(url)
    
    def get_exchange_rate(self, base_currency_code, target_currency_code):
        url = f'{self.base_url}/currencies/{base_currency_code.lower()}/{target_currency_code.lower()}.json'
        return get_response(url)

def table_row(data):
    table = PrettyTable(["Currency Name"],title="Currency Details")
    for curr in data:
        table.add_row([curr])
    print(table)


def main():
    currency = Currency()
    parser = argparse.ArgumentParser()
    parser.add_argument("-list_all","-l",action="store_true", help="List all the available currencies")
    parser.add_argument("-currency_value","-c", help="Enter the currency code to get the value in other currencies")
    parser.add_argument("-get_exchange_rate","-g",action="store_true",  help="Enter the base currency and target currency to get the exchange rate")

    args = parser.parse_args()

    list_all = args.list_all
    currency_value = args.currency_value
    get_exchange_rate = args.get_exchange_rate

    if list_all:
        response = currency.list_currencies()
        if response.status_code == 200:
            print('Success!')
            table = PrettyTable(["Currency Name"],title="Currency Details")
            data = response.json()
            for curr in data:
                table.add_row([curr])
            print(table)
        elif response.status_code == 404:
            print('Not Found.')

    elif currency_value:
        response = currency.currency_value_in_others(currency_value)
        if response.status_code == 200:
            print('Success!')
            print(response.json())
        elif response.status_code == 404:
            print('Not Found.')
    
    elif get_exchange_rate:
        base_currency_code = input("Enter the base currency code: ")
        target_currency_code = input("Enter the target currency code: ")
        response = currency.get_exchange_rate(base_currency_code, target_currency_code)
        if response.status_code == 200:
            print('Success!')
            print(response.json())
        elif response.status_code == 404:
            print('Not Found.')
    
    else:
        print("ERROR")

if __name__ == '__main__':
    main()


