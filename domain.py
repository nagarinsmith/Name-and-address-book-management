class Activity:
    """
    For of storing activity information
    """

    def __init__(self, Id, personIds, date, time, description):
        self.__Id = Id
        self.__personIds = personIds
        self.__date = date
        self.__time = time
        self.__description = description

    # Getters and setters

    @property
    def Id(self):
        return self.__Id

    @Id.setter
    def Id(self, Id):
        self.__Id = Id

    @property
    def personIds(self):
        return self.__personIds

    @personIds.setter
    def personIds(self, personIds):
        self.__personIds = personIds

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    def __eq__(self, other):
        if not isinstance(other, Activity):
            return False
        return self.__Id == other.Id

    def __personIdsToPersonString(self):
        """
        Transforms list of ids in string
        :return: String of ids
        """
        string = ""
        for Id in self.__personIds:
            string += str(Id) + ", "
        return string

    def __str__(self):
        """
        :return: String containing details about activity formatted for user
        """
        return "Id: " + str(self.__Id) + \
               ", Person Ids: " + self.__personIdsToPersonString() + \
               "Date: " + str(self.__date) + \
               ", Time: " + str(self.__time) + \
               ", Description: " + self.__description


class Person:
    """
    For storing person information
    """

    def __init__(self, Id, name, phoneNumber, address):
        self.__Id = Id
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__address = address

    # Getters and setters

    @property
    def Id(self):
        return self.__Id

    @Id.setter
    def Id(self, Id):
        self.__Id = Id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def __eq__(self, other):
        """
        Checks if two person objects have the same id
        :param other:
        :return: True if objects are Person and have the same id
        """
        if not isinstance(other, Person):
            return False
        return self.Id == other.Id

    def __str__(self):
        """
        :return: String containing details about activity formatted for user
        """
        return "Id: " + str(self.__Id) + \
               ", Name: " + self.__name + \
               ", Phone Number: " + self.__phoneNumber + \
               ", Address: " + self.__address
