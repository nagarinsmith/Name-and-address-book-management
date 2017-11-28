import re


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
        string += "\t help - List commands\n"
        string += "\t 0 - Exit\n"
        print(string)

    def mainMenu(self):
        UI.__printMenu()
        keepAlive = True
        while keepAlive:
            command = str(input("Command> "))
            if command == '1':
                Id = input("Person id> ")
                try:
                    Id = int(Id)
                except ValueError:
                    raise ValueError("Id must be integer")
                if Id < 0:
                    raise ValueError("Id must be bigger or equal to 0")

                name = str(input("Person name> "))
                if len(name) < 1:
                    raise TypeError("Invalid name")
                nameRule = re.compile(r'[a-zA-Z\s]+$')
                if not nameRule.search(name):
                    raise TypeError("Invalid name")

                phoneNumber = str(input("Person phone number> "))
                if len(phoneNumber) != 10:
                    raise TypeError("Invalid phone number")

                address = str(input("Person address> "))
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

                # TODO-date and time integrity check

                date = str(input("Activity date> "))
                if len(date) < 1:
                    raise TypeError("Must specify activity date")

                time = str(input("Activity time> "))
                if len(time) < 1:
                    raise TypeError("Must specify activity time")

                description = str(input("Activity description: "))
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

                name = str(input("Person name> "))
                if len(name) < 1:
                    raise TypeError("Invalid name")
                nameRule = re.compile(r'[a-zA-Z\s]+$')
                if not nameRule.search(name):
                    raise TypeError("Invalid name")

                phoneNumber = str(input("Person phone number> "))
                if len(phoneNumber) != 10:
                    raise TypeError("Invalid phone number")

                address = str(input("Person address> "))
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

                # TODO-date and time integrity check

                date = str(input("Activity date> "))
                if len(date) < 1:
                    raise TypeError("Must specify activity date")

                time = str(input("Activity time> "))
                if len(time) < 1:
                    raise TypeError("Must specify activity time")

                description = str(input("Activity description: "))
                if len(description) < 1:
                    raise TypeError("Must specify activity description")

                self.__activityController.update(Id, personIds, date, time, description)
                print("\nCommand executed successfully!\n")

            elif command == '7':
                print(self.__personController.list())

            elif command == '8':
                print(self.__activityController.list())

            elif command == '0':
                keepAlive = False

            elif command == 'help':
                UI.__printMenu()

            else:
                raise TypeError("Invalid command")
