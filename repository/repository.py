class Repository:
    def __init__(self):
        """
        Constructor for PersonRepository class
        """
        self.__data = []

    def add(self, element):
        """
        Add a element to the repository
        :param element: Element to be added
        :return:
        """
        self.__data.append(element)
