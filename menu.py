import re
import datetime


class UI:
    def __init__(self, personController, activityController):
        self.__personController = personController
        self.__activityController = activityController

    @staticmethod
    def __printMenu():
        string = "\n Available commands:\n"
        string += "\t 1 - Add person\n"
        string += "\t 2 - Add activity\n"
        string += "\t 3 - Remove person\n"
        string += "\t 4 - Remove activity\n"
        string += "\t 5 - Update person\n"
        string += "\t 6 - Update activity\n"
        string += "\t 7 - List persons\n"
        string += "\t 8 - List activities\n"
        string += "\t 9 - Search persons\n"
        string += "\t 10 - Search activities\n"
        string += "\t help - List commands\n"
        string += "\t 0 - Exit\n"
        print(string)

    def mainMenu(self):
        UI.__printMenu()
        keepAlive = True
        while keepAlive:
            command = input("Command> ")
            if command == '1':
                Id = input("Person id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")

                name = input("Person name> ")
                if len(name) < 1:
                    raise TypeError("Invalid name")
                nameRule = re.compile(r'[a-zA-Z\s]+$')
                if not nameRule.search(name):
                    raise TypeError("Invalid name")

                phoneNumber = input("Person phone number> ")
                if len(phoneNumber) != 10:
                    raise TypeError("Invalid phone number")

                address = input("Person address> ")
                if len(address) < 7:
                    raise TypeError("Invalid address")

                self.__personController.create(Id, name, phoneNumber, address)
                print("\nCommand executed successfully!\n")
            elif command == '2':
                Id = input("Activity id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")

                personIds = input("Person ids> ").split()
                if not personIds:
                    raise TypeError("Must specify person ids")
                for i in range(len(personIds)):
                    try:
                        personIds[i] = int(personIds[i])
                    except ValueError:
                        raise ValueError("Invalid person ids")

                # reading date
                print("Reading date..")
                year = input("Year> ")
                month = input("Month (1-12)> ")
                day = input("Day> ")
                try:
                    year = int(year)
                    month = int(month)
                    day = int(day)
                except ValueError:
                    raise ValueError("Invalid date")
                date = datetime.date(year, month, day)

                # reading time
                print("Reading time..")
                hour = input("Hour> ")
                minutes = input("Minutes> ")
                try:
                    hour = int(hour)
                    minutes = int(minutes)
                except ValueError:
                    raise ValueError("Invalid time")
                time = datetime.time(hour, minutes)

                description = input("Activity description: ")
                if len(description) < 1:
                    raise TypeError("Must specify activity description")

                self.__activityController.create(Id, personIds, date, time, description)
                print("\nCommand executed successfully!\n")

            elif command == '3':
                Id = input("Person id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")
                self.__personController.delete(Id)
                print("\nCommand executed successfully!\n")

            elif command == '4':
                Id = input("Activity id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")
                self.__activityController.delete(Id)
                print("\nCommand executed successfully!\n")

            elif command == '5':
                Id = input("Person id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")

                name = input("Person name> ")
                if len(name) < 1:
                    raise TypeError("Invalid name")
                nameRule = re.compile(r'[a-zA-Z\s]+$')
                if not nameRule.search(name):
                    raise TypeError("Invalid name")

                phoneNumber = input("Person phone number> ")
                if len(phoneNumber) != 10:
                    raise TypeError("Invalid phone number")

                address = input("Person address> ")
                if len(address) < 7:
                    raise TypeError("Invalid address")

                self.__personController.update(Id, name, phoneNumber, address)
                print("\nCommand executed successfully!\n")

            elif command == '6':
                Id = input("Activity id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")

                personIds = input("Person ids> ").split()
                if not personIds:
                    raise TypeError("Must specify person ids")
                for i in range(len(personIds)):
                    try:
                        personIds[i] = int(personIds[i])
                    except ValueError:
                        raise ValueError("Invalid person ids")

                print("Reading date..")
                year = input("Year> ")
                month = input("Month (1-12)> ")
                day = input("Day> ")
                try:
                    year = int(year)
                    month = int(month)
                    day = int(day)
                except ValueError:
                    raise ValueError("Invalid date")
                date = datetime.date(year, month, day)

                print("Reading time..")
                hour = input("Hour> ")
                minutes = input("Minutes> ")
                try:
                    hour = int(hour)
                    minutes = int(minutes)
                except ValueError:
                    raise ValueError("Invalid time")
                time = datetime.time(hour, minutes)

                description = input("Activity description: ")
                if len(description) < 1:
                    raise TypeError("Must specify activity description")

                self.__activityController.update(Id, personIds, date, time, description)
                print("\nCommand executed successfully!\n")

            elif command == '7':
                print(self.__personController.list())

            elif command == '8':
                print(self.__activityController.list())

            elif command == '9':
                string = "\nCriteria:\n"
                string += "\t1 - Name\n"
                string += "\t2 - Phone Number\n"
                print(string)
                command = input("Command> ")
                try:
                    command = int(command)
                except ValueError:
                    raise ValueError("Invalid command")
                if command == 1 or 2:
                    searchTerm = input("Criteria> ")
                else:
                    raise TypeError("Invalid command")
                print(self.__personController.search(command, searchTerm))

            elif command == '10':
                string = "\nCriteria:\n"
                string += "\t1 - Date\n"
                string += "\t2 - Time\n"
                string += "\t3 - Description\n"
                print(string)
                command = input("Command> ")
                if command == '1':
                    print("Reading date..")
                    year = input("Year> ")
                    month = input("Month (1-12)> ")
                    day = input("Day> ")
                    try:
                        year = int(year)
                        month = int(month)
                        day = int(day)
                    except ValueError:
                        raise ValueError("Invalid date")
                    searchTerm = datetime.date(year, month, day)

                elif command == '2':
                    print("Reading time..")
                    hour = input("Hour> ")
                    minutes = input("Minutes> ")
                    try:
                        hour = int(hour)
                        minutes = int(minutes)
                    except ValueError:
                        raise ValueError("Invalid time")
                    searchTerm = datetime.time(hour, minutes)

                elif command == '3':
                    searchTerm = input("Criteria> ")
                else:
                    raise TypeError("invalid command")
                print(self.__activityController.search(command, searchTerm))

            elif command == '0':
                keepAlive = False

            elif command == 'help':
                UI.__printMenu()

            else:
                raise TypeError("Invalid command")
