from bruteforce_engine import engine
from data_reader import reader
from reporter import save_results_to_json
from datetime import datetime

def main():
    word_list, username_list = reader()
    result = engine(word_list, username_list)
    save_results_to_json(result)

if __name__ == "__main__":

    main()
    if False:
        save_results_to_json(
            {
                "pekka": {
                    "bool": True,
                    "password": "1234",
                    "timestamp": datetime.now()
                },
                "lauri": {
                    "bool": False,
                    "password": "popo",
                    "timestamp": datetime.now()
                }
                }
        )