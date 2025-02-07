import json
from .TransactionManagementException import TransactionManagementException
from .TransactionRequest import TransactionRequest

class TransactionManager:
    def __init__(self):
        pass

    def validate_iban(self, iban : str) -> bool:
        """A method that checks if an iban is correct or not"""
        if len(iban) != 24 or iban[:2] != 'ES' or not iban[2:].isdigit(): return False

        iban = iban[4:] + iban[:4]
        numeric_iban = ''

        for char in iban:
            if not char.isalpha():
                numeric_iban += char
            else:
                numeric_iban += (str(ord(char) - 55))

        if int(numeric_iban) % 97 == 1:
            return True
        return False

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise TransactionManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise TransactionManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            T_FROM = DATA["from"]
            T_TO = DATA["to"]
            TO_NAME = DATA["recipient_name"]
            req = TransactionRequest(T_FROM, T_TO,TO_NAME)
        except KeyError as e:
            raise TransactionManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validate_iban(T_FROM) :
            raise TransactionManagementException("Invalid FROM IBAN")
        else:
            if not self.validate_iban(T_TO):
                raise TransactionManagementException("Invalid TO IBAN")
        return req
