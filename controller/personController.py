class Person:
    def __init__(self, personId, name, phoneNumber, address):
        self.__personId = personId
        self.__Name = name
        self.__PhoneNumber = phoneNumber
        self.__address = address

    def setPersonId(self, personId):
        self.__personId = personId

    def getPersonId(self):
        return self.__personId

    def setName(self, name):
        self.__Name = name

    def getName(self):
        return self.__Name

    def setPhoneNumber(self, phoneNumber):
        self.__PhoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.__PhoneNumber

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address
