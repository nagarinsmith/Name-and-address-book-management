import datetime

from collections import Counter

from domain import Person, Activity

from validators import PersonValidator, ActivityValidator

from repository import Repository

from exceptions import RepositoryException


class PersonService:
    """
    Bridge between ui and repo
    """

    def __init__(self, activityRepository, personRepository):
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
        # delete person ID from all activities in which it's present
        indexOffset = 0
        for i in range(len(self.__activityRepository.getAll())):
            if Id in self.__activityRepository.getAll()[i - indexOffset].personIds:
                self.__activityRepository.getAll()[i - indexOffset].personIds.remove(Id)
            if len(self.__activityRepository.getAll()[i - indexOffset].personIds) == 0:
                self.__activityRepository.delete(self.__activityRepository.getAll()[i - indexOffset].Id)
                indexOffset += 1

        self.__personRepository.delete(Id)

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
        if criteria == '1':
            for person in self.__personRepository.getAll():
                if searchTerm in person.name:
                    searchRepo.store(person)
        elif criteria == '2':
            for person in self.__personRepository.getAll():
                if searchTerm in person.phoneNumber:
                    searchRepo.store(person)
        return searchRepo


class ActivityService:
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
        if criteria == '1':
            for activity in self.__activityRepository.getAll():
                if searchTerm == activity.date:
                    searchRepo.store(activity)
        elif criteria == '2':
            for activity in self.__activityRepository.getAll():
                if searchTerm == activity.time:
                    searchRepo.store(activity)
        elif criteria == '3':
            for activity in self.__activityRepository.getAll():
                if searchTerm in activity.description:
                    searchRepo.store(activity)
        return searchRepo

    def dayOfWeekActivities(self, day):
        activitiesList = []
        for activity in self.__activityRepository.getAll():
            if activity.date.weekday() == day:
                activitiesList.append(activity)
        activitiesList = sorted(activitiesList, key=lambda x: (x.date, x.time))
        activitiesRepo = Repository()
        for activity in activitiesList:
            activitiesRepo.store(activity)
        return activitiesRepo

    def busiestDays(self):
        dateList = []
        for activity in self.__activityRepository.getAll():
            if activity.date > datetime.date.today():
                dateList.append(str(activity.date))
        sortedDateList = [item for items, c in Counter(dateList).most_common() for item in [items] * c]
        dateSet = self.uniquedList(sortedDateList)
        dateString = '\n' + '\n'.join(dateSet) + '\n'
        return dateString

    def activitiesWithPerson(self, personId):
        if self.__personRepository.find(personId) is None:
            raise RepositoryException("Person does not exist in repository")
        activitiesWithPersonRepo = Repository()
        for activity in self.__activityRepository.getAll():
            if personId in activity.personIds:
                activitiesWithPersonRepo.store(activity)
        return activitiesWithPersonRepo

    def sortedPersons(self):
        idList = []
        for activity in self.__activityRepository.getAll():
            idList.extend(activity.personIds)
        sortedIdList = [item for items, c in Counter(idList).most_common() for item in [items] * c]
        print(sortedIdList)
        idSet = self.uniquedList(sortedIdList)
        print(idSet)
        sortedPersonsRepo = Repository()
        for ID in idSet:
            sortedPersonsRepo.store(self.__personRepository.find(ID))
        return sortedPersonsRepo

    @staticmethod
    def uniquedList(originalList):
        uniquedList = [originalList[0]]
        for i in range(1, len(originalList)):
            if originalList[i] != originalList[i - 1]:
                uniquedList.append(originalList[i])
        return uniquedList
