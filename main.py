from bruteforce_engine import engine
from data_reader import reader
from reporter import save_results_to_json

def main():
    word_list, username_list = reader()
    result = engine(word_list, username_list)
    save_results_to_json(result)

if __name__ == "__main__":

    main()