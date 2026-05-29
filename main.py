from bruteforce_engine import engine
from wordlist_reader import reader

def main():
    wordlist = reader()
    result = engine(wordlist)

if __name__ == "__main__":
    main()