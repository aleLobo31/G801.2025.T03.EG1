from UC3MMoney import TransactionManager
import string

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3

def ejemplo_funcion(a):
    if(a > 3):
        if(a > 6):
            if(a > 9):
                if(a > 12):
                    if(a > 15):
                        print(a)

def Encode(word) -> str:
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

    mng = TransactionManager()
    res = mng.ReadproductcodefromJSON("test.json")
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