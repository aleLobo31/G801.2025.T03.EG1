from UC3MMoney import transactionManager
import string

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3
test_files = ["valid_test.json", "invalid_test.json"]

# Este es un comentario que supera con creces los 120 caracteres porque sigue extendién-dose más allá del límite definido para ilustrar el caso correctamente.

def f(a, b, c, d, e, f, g):
    pass

def my_function() -> None:
    x = 1
    y = 2
    print("Posicion: x = {}, y = {}".format(x, y))
    return

def ejemplo_funcion(a):
    if(a > 3):
        if(a > 6):
            if(a > 9):
                if(a > 12):
                    if(a > 15):
                        print(a)

    try:
        x = 1 / 0
    except:
        print("Se ha producido un error")

def analizar_datos(valor: int) -> str:
    if valor == 1:
        return "Uno"
    elif valor == 2:
        return "Dos"
    elif valor == 3:
        return "Tres"
    elif valor == 4:
        return "Cuatro"
    elif valor == 5:
        return "Cinco"
    elif valor == 6:
        return "Seis"
    elif valor == 7:
        return "Siete"
    elif valor == 8:
        return "Ocho"
    else:
        return "Otro"

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
        mng = transactionManager()
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