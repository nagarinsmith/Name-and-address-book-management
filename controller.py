from domain import Person, Activity
from validators import PersonValidator, ActivityValidator
from repository import Repository


class PersonController:
    """
    Bridge between ui and repo
    """
    def __init__(self, personRepository, activityRepository):
        self.__personRepository = personRepository
        self.__activityRepository = activityRepository

    def create(self, Id, name, phoneNumber, address):
        """
        Adds person to person repo
        :param Id:
        :param name:
        :param phoneNumber:
        :param address:
        :return:
        """
        person = Person(Id, name, phoneNumber, address)
        PersonValidator.validate(person)
        self.__personRepository.store(person)

    def delete(self, Id):
        """
        Deletes person from person repo
        :param Id:
        :return:
        """
        # TODO-remove activities which contained the deleted person id
        self.__activityRepository.delete(Id)

    def update(self, Id, name, phoneNumber, address):
        """
        Updates person from person repo
        :param Id:
        :param name:
        :param phoneNumber:
        :param address:
        :return:
        """
        person = Person(Id, name, phoneNumber, address)
        PersonValidator.validate(person)
        self.__personRepository.update(person)

    def list(self):
        """
        Passes person repo
        :return:
        """
        return self.__personRepository

    def search(self, criteria, searchTerm):
        """
        Searches persons based on name or phone number
        :param criteria: name/phone number
        :param searchTerm:
        :return:
        """
        searchRepo = Repository()
        if criteria == 1:
            for person in self.__personRepository.getAll():
                if searchTerm in person.name:
                    searchRepo.store(person)
        elif criteria == 2:
            for person in self.__personRepository.getAll():
                if searchTerm in person.phoneNumber:
                    searchRepo.store(person)
        return searchRepo


class ActivityController:
    """
    Bridge between ui and repo
    """
    def __init__(self, activityRepository, personRepository):
        self.__activityRepository = activityRepository
        self.__personRepository = personRepository

    def create(self, Id, personIds, date, time, description):
        """
        Adds activity to activity repo
        :param Id:
        :param personIds:
        :param date:
        :param time:
        :param description:
        :return:
        """
        activity = Activity(Id, personIds, date, time, description)
        ActivityValidator.validate(activity, self.__activityRepository, self.__personRepository)
        self.__activityRepository.store(activity)

    def delete(self, Id):
        """
        Removes activity from activity repo
        :param Id:
        :return:
        """
        self.__activityRepository.delete(Id)

    def update(self, Id, personIds, date, time, description):
        """
        Updates activity from activity repo
        :param Id:
        :param personIds:
        :param date:
        :param time:
        :param description:
        :return:
        """
        activity = Activity(Id, personIds, date, time, description)
        ActivityValidator.validate(activity, self.__activityRepository, self.__personRepository)
        self.__activityRepository.update(activity)

    def list(self):
        """
        Passes activity repo
        :return:
        """
        return self.__activityRepository

    def search(self, criteria, searchTerm):
        """
        Searches activities based on date time or description
        :param criteria: date/time/description
        :param searchTerm:
        :return:
        """
        searchRepo = Repository()
        if criteria == 1:
            for activity in self.__activityRepository.getAll():
                if searchTerm in activity.date:
                    searchRepo.store(activity)
        elif criteria == 2:
            for activity in self.__activityRepository.getAll():
                if searchTerm in activity.time:
                    searchRepo.store(activity)
        elif criteria == 3:
            for activity in self.__activityRepository.getAll():
                if searchTerm in activity.time:
                    searchRepo.store(activity)
        return searchRepo
