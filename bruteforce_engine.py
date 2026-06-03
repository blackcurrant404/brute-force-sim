import requests

url = "http://127.0.0.1:5000/login"

def engine(word_list: list, username_list: list):
    for username in username_list:
        for password in word_list:
            payload = {
                "username": "root",
                "password": password

            }
            
            response = requests.post(url, data=payload)
            if is_login_successful(response):
                print("FOUND")
                break

    return None

def is_login_successful(response):
    return "successful" in response.text
