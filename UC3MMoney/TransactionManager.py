""" Import required modules"""
import json
from .TransactionManagementException import TransactionManagementException
from .TransactionRequest import TransactionRequest

class TransactionManager:
    """Class define to handle incoming transactions"""
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

    def read_product_code_from_json(self, file):
        """A method that reads recipient and sender from a JSON and checks whether the iban is ok"""
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise TransactionManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise TransactionManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            t_from = data["from"]
            t_to = data["to"]
            to_name = data["recipient_name"]
            request = TransactionRequest(t_from, t_to,to_name)
        except KeyError as e:
            raise TransactionManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validate_iban(t_from):
            raise TransactionManagementException("Invalid FROM IBAN")
        if not self.validate_iban(t_to):
            raise TransactionManagementException("Invalid TO IBAN")
        print("Valid IBAN")
        return request
