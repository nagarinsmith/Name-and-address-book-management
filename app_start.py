from repository import Repository
from service import PersonService, ActivityService
from menu import UI
import datetime


# Initialising repos
activityRepo = Repository()
personRepo = Repository()
# Initialising controllers
personService = PersonService(personRepo, activityRepo)
activityService = ActivityService(activityRepo, personRepo)
# 10 initial values
personService.create(1, 'Paul Orha', '0745616223', 'Str. George Cosbuc 35/46, Baia Mare, Romania')
personService.create(2, 'Stoica Andrei', '0742913234', 'Str. exemplu 1/2, Cluj, Romania')
personService.create(3, 'Miclaus Marcel', '0745966527', 'Str. exemplu 3/4, Buzau, Romania')
personService.create(4, 'David Buzila', '0745918209', 'Str. exemplu 5/6, Sibiu, Romania')
personService.create(5, 'Ion Demonstrare', '0764928109', 'Str. exemplu 6/7, Galati, Romania')
activityService.create(1, [1], datetime.date(2017, 11, 30), datetime.time(0, 0), 'Sample description1')
activityService.create(2, [1, 2], datetime.date(2017, 12, 1), datetime.time(15, 42), 'Sample description2')
activityService.create(3, [1, 2, 3], datetime.date(2018, 1, 2), datetime.time(14, 30), 'Sample description3')
activityService.create(4, [2, 5], datetime.date(2018, 1, 5), datetime.time(14, 45), 'Sample description4')
activityService.create(5, [4, 5], datetime.date(2018, 2, 2), datetime.time(12, 0), 'Sample description5')
# initialising ui
ux = UI(personService, activityService)
# running user interface
ux.mainMenu()
