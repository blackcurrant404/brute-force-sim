from bruteforce_engine import engine
from wordlist_reader import reader

def main():
    wordlist = reader()
    result = engine(wordlist)

    if result == "":
        print("coudn't fint the password, try different wordlist")
    else:
        print("The correct password is", result)

if __name__ == "__main__":
    main()