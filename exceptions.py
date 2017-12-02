class RepositoryException(Exception):
    """
    In case of repository error
    """
    def __init__(self, message):
        self.__message = message

    def getMessage(self):
        return self.__message

    def __str__(self):
        return "\nRepository error:\n>\t" + self.__message + '\n'


class ValidatorException(Exception):
    """
    In case of validation error
    """
    def __init__(self, messageList):
        self.__messageList = messageList

    def getMessage(self):
        return self.__messageList

    def __str__(self):
        string = "\nValidation error:\n"
        for message in self.getMessage():
            string += '>\t' + message + '\n'
        return string


class UIException(Exception):
    """
    In case of UI error
    """
    def __init__(self, message):
        self.__message = message

    def getMessage(self):
        return self.__message

    def __str__(self):
        return "\nUI error:\n>\t" + self.__message + '\n'
