from exceptions import RepositoryException


class Repository:
    def __init__(self):
        """
        Constructor for Repository class
        """
        self.__objects = []

    def store(self, obj):
        """
        Add an object to the repository
        :param obj: Object to be added
        :return: None
        """
        if self.find(obj.Id) is not None:
            raise RepositoryException("Object having id " + str(obj.Id) + " already added")
        self.__objects.append(obj)

    def delete(self, objectId):
        """
        Removes object from repository
        :param objectId: Id of object
        :return: None
        """
        obj = self.find(objectId)
        if obj is None:
            raise RepositoryException("Object not in repository")
        self.__objects.remove(obj)
        return obj

    def update(self, obj):
        """
        Replace the object with the new one if having the same id
        :param obj: Updated object
        :return: None
        """
        repoObject = self.find(obj.Id)
        if repoObject is None:
            raise RepositoryException("Object not in repository")
        repoObjectIndex = self.__objects.index(repoObject)
        self.__objects.remove(repoObject)
        self.__objects.insert(repoObjectIndex, obj)

    def find(self, objectId):
        """
        Finds object based on object id
        :param objectId:
        :return: Object if found else None
        """
        for obj in self.__objects:
            if objectId == obj.Id:
                return obj
        return None

    def getAll(self):
        """
        Returns all objects from repository
        :return: List of objects
        """
        return self.__objects

    def __len__(self):
        """
        Returns the size of the repository
        :return: Size of repository
        """
        return len(self.__objects)

    def __str__(self):
        """
        All objects from repository formated for user
        :return: String of objects
        """
        string = '\n'
        for obj in self.__objects:
            string += str(obj) + '\n'
        return string
