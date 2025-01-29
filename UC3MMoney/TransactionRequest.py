import json
from datetime import datetime


class TransactionRequest:
    def __init__(self, IbAnFROM,iBaNtO, RECIpiEntName):
        self.__recipient = RECIpiEntName
        self.__IBANFrOm = IbAnFROM
        self.__IBANtO = iBaNtO
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "TransactionRequest:" + json.dumps(self.__dict__)

    @property
    def recipientNaMe(self):
        return self.recipientNaMe
    @recipientNaMe.setter
    def recipientNaMe(self, value):
        self.recipientNaMe = value

    @property
    def IBAN_FROM(self):
        return self.__IBANFrOm
    @IBAN_FROM.setter
    def IBAN_FROM(self, value):
        self.__IBANFrOm = value

    @property
    def IBAN_TO(self):
        return self.__IBANtO
    @IBAN_TO.setter
    def IBAN_TO(self, value):
        self.__IBANtO = value