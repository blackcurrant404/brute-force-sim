from bruteforce_engine import engine
from wordlist_reader import reader

def main():
    word_list, username_list = reader()
    result = engine(word_list, username_list)

    if result is None:
        print("coudn't fint the password, try different wordlist")
    else:
        print("The correct password is", result)

if __name__ == "__main__":
    main()