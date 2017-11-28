from domain import Person, Activity
from validators import PersonValidator, ActivityValidator


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
