from UC3MMoney import TransactionManager
import string

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3
test_files = ["valid_test.json", "invalid_test.json"]

def Encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) + shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def Decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) - shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded


def main():
    for i in range(2):
        mng = TransactionManager()
        res = mng.ReadproductcodefromJSON(test_files[i])
        strRes = res.__str__()
        print(strRes)
        EncodeRes = Encode(strRes)
        print("Encoded Res "+ EncodeRes)
        DecodeRes = Decode(EncodeRes)
        print("Decoded Res: " + DecodeRes)
        print("IBAN_FROM: " + res.IBAN_FROM)
        print("IBAN_TO: " + res.IBAN_TO)

if __name__ == "__main__":
    main()