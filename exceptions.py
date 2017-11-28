class RepositoryException(Exception):
    """
    In case of repository error
    """
    def __init__(self, message="Repository error"):
        self.__message = message

    def getMessage(self):
        return self.__message

    def __str__(self):
        return self.__message


class ValidatorException(Exception):
    """
    In case of validation error
    """
    def __init__(self, messageList="Validation error"):
        self.__messageList = messageList

    def getMessage(self):
        return self.__messageList

    def __str__(self):
        string = ""
        for message in self.getMessage():
            string += message + '\n'
        return string
