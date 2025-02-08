""" Import required modules"""
import json
#from datetime import datetime


class TransactionRequest:
    """Class to store transaction associated data: recipient, and both required iban"""
    def __init__(self, iban_from, iban_to, recipient_name) -> None:
        self.__recipient = recipient_name
        self.__iban_from = iban_from
        self.__iban_to = iban_to
        #justnow = datetime.utcnow()
        #self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "TransactionRequest:" + json.dumps(self.__dict__)

    @property
    def recipient(self):
        return self.__recipient
    @recipient.setter
    def recipient(self, value):
        self.__recipient = value

    @property
    def iban_from(self):
        return self.__iban_from
    @iban_from.setter
    def iban_from(self, value):
        self.__iban_from = value

    @property
    def iban_to(self):
        return self.__iban_to
    @iban_to.setter
    def iban_to(self, value):
        self.__iban_to = value
