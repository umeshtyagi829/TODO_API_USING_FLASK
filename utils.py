import requests
import json

def get_response(url):
    try:
        response = requests.get(url) 
    except requests.ConnectTimeout:
        return " Request timeout"
    except requests.ConnectionError:
        return "Connection failed please check your internet connection" 
    except Exception as e:
        return f'Something went wrong {e}' 

    if response.status_code == 200:
        return response
       
    else:
        res = requests.Response()
        res.status_code = response.status_code
        utf_string = '{"error": "Invalid currency code"}'
        bytes_string = utf_string.encode('utf-8')
        res._content = bytes_string
        return res
 


