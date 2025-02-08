""" Import required modules"""
import string
from UC3MMoney import TransactionManager

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3
test_files = ["valid_test.json", "invalid_test.json"]


def encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded


def decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded


def main():
    """Create an instance of TransactionManager to test it"""
    for i in range(2):
        mng = TransactionManager()
        res = mng.read_product_code_from_json(test_files[i])
        str_res = str(res)
        print(str_res)
        encode_res = encode(str_res)
        print("Encoded Res "+ encode_res)
        decode_res = decode(encode_res)
        print("Decoded Res: " + decode_res)
        print("IBAN_FROM: " + res.iban_from)
        print("IBAN_TO: " + res.iban_to)


if __name__ == "__main__":
    main()
