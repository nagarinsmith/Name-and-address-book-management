import datetime

from exceptions import UIException

import sys


class UI:
    def __init__(self, personService, activityService):
        self.__personService = personService
        self.__activityService = activityService

    @staticmethod
    def __printMenu():
        string = "\nAvailable commands:\n"
        string += "\t1 - Add person\n"
        string += "\t2 - Add activity\n"
        string += "\t3 - Remove person\n"
        string += "\t4 - Remove activity\n"
        string += "\t5 - Update person\n"
        string += "\t6 - Update activity\n"
        string += "\t7 - List persons\n"
        string += "\t8 - List activities\n"
        string += "\t9 - Search persons\n"
        string += "\t10 - Search activities\n"
        string += "\t11 - Create statistics\n"
        string += "\thelp - List commands\n"
        string += "\t0 - Exit\n"
        print(string)

    def menu(self):
        self.__printMenu()

        commandDictionary = {'1': self.__addPerson,
                             '2': self.__addActivity,
                             '3': self.__removePerson,
                             '4': self.__removeActivity,
                             '5': self.__updatePerson,
                             '6': self.__updateActivity,
                             '7': self.__listPersons,
                             '8': self.__listActivities,
                             '9': self.__searchPersons,
                             '10': self.__searchActivities,
                             '11': self.__statisticsSubMenu,
                             '0': self.__exit,
                             'help': self.__printMenu}

        while True:

            command = input("Command> ")

            try:
                commandDictionary[command]()

            except KeyError:
                print("\033[93m" + str(UIException("Invalid command")) + "\033[0m")
            except Exception as ex:
                print("\033[93m" + str(ex) + "\033[0m")

    def __addPerson(self):
        Id = input("Person id> ")
        try:
            Id = int(Id)
        except ValueError:
            raise UIException("Id must be integer")
        name = input("Person name> ")
        phoneNumber = input("Person phone number> ")
        address = input("Person address> ")
        self.__personService.create(Id, name, phoneNumber, address)
        print("\nCommand executed successfully!\n")

    def __addActivity(self):
        Id = input("Activity id> ")
        try:
            Id = int(Id)
        except ValueError:
            raise UIException("Id must be integer")
        personIds = input("Person ids> ").split()
        for i in range(len(personIds)):
            try:
                personIds[i] = int(personIds[i])
            except ValueError:
                raise UIException("Invalid person ids")
        date = self.__readDate()
        time = self.__readTime()
        description = input("Activity description: ")
        self.__activityService.create(Id, personIds, date, time, description)
        print("\nCommand executed successfully!\n")

    def __removePerson(self):
        Id = input("Person id> ")
        try:
            Id = int(Id)
        except ValueError:
            raise UIException("Id must be integer")
        self.__personService.delete(Id)
        print("\nCommand executed successfully!\n")

    def __removeActivity(self):
        Id = input("Activity id> ")
        try:
            Id = int(Id)
        except ValueError:
            raise UIException("Id must be integer")
        self.__activityService.delete(Id)
        print("\nCommand executed successfully!\n")

    def __updatePerson(self):
        Id = input("Person id> ")
        try:
            Id = int(Id)
        except ValueError:
            raise UIException("Id must be integer")
        name = input("Person name> ")
        phoneNumber = input("Person phone number> ")
        address = input("Person address> ")
        self.__personService.update(Id, name, phoneNumber, address)
        print("\nCommand executed successfully!\n")

    def __updateActivity(self):
        Id = input("Activity id> ")
        try:
            Id = int(Id)
        except ValueError:
            raise UIException("Id must be integer")
        personIds = input("Person ids> ").split()
        date = self.__readDate()
        time = self.__readTime()
        description = input("Activity description: ")
        self.__activityService.update(Id, personIds, date, time, description)
        print("\nCommand executed successfully!\n")

    def __listPersons(self):
        print(self.__personService.list())

    def __listActivities(self):
        print(self.__activityService.list())

    def __searchPersons(self):
        string = "\nCriteria:\n"
        string += "\t1 - Name\n"
        string += "\t2 - Phone Number\n"
        print(string)
        command = input("Command> ")
        if command in ('1', '2'):
            searchTerm = input("Criteria> ")
        else:
            raise UIException("Invalid command")
        print(self.__personService.search(command, searchTerm))

    def __searchActivities(self):
        string = "\nCriteria:\n"
        string += "\t1 - Date\n"
        string += "\t2 - Time\n"
        string += "\t3 - Description\n"
        print(string)
        command = input("Command> ")
        if command == '1':
            searchTerm = self.__readDate()
        elif command == '2':
            searchTerm = self.__readTime()
        elif command == '3':
            searchTerm = input("Criteria> ")
        else:
            raise UIException("invalid command")
        print(self.__activityService.search(command, searchTerm))

    @staticmethod
    def __printStatisticsSubMenu():
        string = "\nStatistics:\n"
        string += "\t1 - Activities for a given day/week\n"
        string += "\t2 - Busiest days\n"
        string += "\t3 - Activities with a given person\n"
        string += "\t4 - List all persons sorted by number of activities\n"
        print(string)

    def __statisticsSubMenu(self):
        self.__printStatisticsSubMenu()
        commandDictionary = {'1': self.__dayOfWeekActivities,
                             '2': self.__busiestDays,
                             '3': self.__activitiesWithPerson,
                             '4': self.__sortedPersons}
        command = input("Command> ")
        try:
            commandDictionary[command]()
        except KeyError:
            raise UIException("Invalid command")

    def __dayOfWeekActivities(self):
        dayOfWeek = input("Day of week(0-6)> ")
        try:
            dayOfWeek = int(dayOfWeek)
        except ValueError:
            raise UIException("Invalid day of week")
        if 0 >= dayOfWeek >= 6:
            raise UIException("Invalid day of week")
        print(self.__activityService.dayOfWeekActivities(dayOfWeek))

    def __busiestDays(self):
        print(self.__activityService.busiestDays())

    def __activitiesWithPerson(self):
        personId = input("Person id> ")
        try:
            personId = int(personId)
        except ValueError:
            raise UIException("Invalid person id")
        print(self.__activityService.activitiesWithPerson(personId))

    def __sortedPersons(self):
        print(self.__activityService.sortedPersons())

    @staticmethod
    def __readDate():
        print("Reading date..")
        year = input("Year> ")
        month = input("Month (1-12)> ")
        day = input("Day> ")
        try:
            year = int(year)
            month = int(month)
            day = int(day)
        except ValueError:
            raise UIException("Invalid date")
        return datetime.date(year, month, day)

    @staticmethod
    def __readTime():
        print("Reading time..")
        hour = input("Hour> ")
        minutes = input("Minutes> ")
        try:
            hour = int(hour)
            minutes = int(minutes)
        except ValueError:
            raise UIException("Invalid time")
        return datetime.time(hour, minutes)

    @staticmethod
    def __exit():
        sys.exit()
