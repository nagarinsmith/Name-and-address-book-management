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
        errorList = []

        if person.Id < 0:
            errorList.append("Id must be bigger or equal than 0")

        if len(person.name) == 0:
            errorList.append("Name not specified")
        nameRule = re.compile(r'[a-zA-Z\s]+$')

        if not nameRule.search(person.name):
            errorList.append("Invalid name")

        if not PersonValidator.__isPhoneNumberValid(person.phoneNumber):
            errorList.append("Phone number is not valid")

        if len(person.address) == 0:
            errorList.append("Address not specified")

        if len(errorList) != 0:
            raise ValidatorException(errorList)


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
        errorList = []

        if activity.Id < 0:
            errorList.append("Id must be bigger or equal to 0")

        if not activity.personIds:
            errorList.append("Person ids not specified")

        if len(activity.description) == 0:
            errorList.append("Description not specified")
        # check if person ids in activity exist
        for Id in activity.personIds:
            if personRepo.find(Id) is None:
                errorList.append("Some persons are not in address book")
                break
        # check if activities overlap on date or time
        for activityRepoActivity in activityRepo.getAll():
            if activity.date == activityRepoActivity.date and activity.time == activityRepoActivity.time:
                errorList.append("Activities must not overlap")
                break

        if len(errorList) != 0:
            raise ValidatorException(errorList)
