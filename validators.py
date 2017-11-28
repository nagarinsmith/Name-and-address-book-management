from domain import Person, Activity
from exceptions import ValidatorException
import re


class PersonValidator:
    """
    Validates person object
    """
    @staticmethod
    def __isPhoneNumberValid(phoneNumber):
        """
        Validates phone number format
        :param phoneNumber:
        :return:
        """
        rule = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')
        if not rule.search(phoneNumber):
            return False
        return True

    @staticmethod
    def validate(person):
        """
        Method of validating person object
        :param person:
        :return:
        """
        if not isinstance(person, Person):
            raise TypeError("Not a person")
        __errorList = []
        if not PersonValidator.__isPhoneNumberValid(person.phoneNumber):
            __errorList.append("Phone number is not valid")
        if len(person.name) == 0:
            __errorList.append("Name is not valid")
        if len(person.address) == 0:
            __errorList.append("Address is not valid")
        if len(__errorList) != 0:
            raise ValidatorException(__errorList)


class ActivityValidator:
    """
    Validates activity object
    """
    @staticmethod
    def validate(activity, activityRepo, personRepo):
        """
        Method of validating activity object
        :param activity:
        :param activityRepo:
        :param personRepo:
        :return:
        """
        if not isinstance(activity, Activity):
            raise TypeError("Not an activity")
        __errorList = []
        for Id in activity.personIds:
            if personRepo.find(Id) is None:
                __errorList.append("Some persons are not in address book")
                break
        for activityRepoActivity in activityRepo.getAll():
            if activity.date == activityRepoActivity.date and activity.time == activityRepoActivity.time:
                __errorList.append("Activities must not overlap")
                break
        if len(__errorList) != 0:
            raise ValidatorException(__errorList)