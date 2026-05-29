import sys
import os

sys.path.append(os.path.abspath("../security-login-sim"))
from verification import verify

def engine(word_list: list):
    for word in word_list:
        if verify(word) == "Accepted":
            return word

    return None