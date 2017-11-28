from repository import Repository
from controller import PersonController, ActivityController
from menu import UI


# Initialising repos
activityRepo = Repository()
personRepo = Repository()
# Initialising controllers
personController = PersonController(personRepo, activityRepo)
activityController = ActivityController(activityRepo, personRepo)
# 10 initial values
personController.create(1, 'Paul Orha', '0745616223', 'Str. George Cosbuc 35/46, Baia Mare, Romania')
personController.create(2, 'Stoica Andrei', '0742913234', 'Str. exemplu 1/2, Cluj, Romania')
personController.create(3, 'Miclaus Marcel', '0745966527', 'Str. exemplu 3/4, Buzau, Romania')
personController.create(4, 'David Buzila', '0745918209', 'Str. exemplu 5/6, Sibiu, Romania')
personController.create(5, 'Ion Demonstrare', '0764928109', 'Str. exemplu 6/7, Galati, Romania')
activityController.create(1, [1], '30 Nov 2017', '00:00', 'Sample description1')
activityController.create(2, [1, 2], '1 Dec 2017', '15:42', 'Sample description2')
activityController.create(3, [1, 2, 3], '2 Ian 2018', '14:30', 'Sample description3')
activityController.create(4, [2, 5], '5 Ian 2018', '14:45', 'Sample description4')
activityController.create(5, [4, 5], '2 Feb 2018', '12:00', 'Sample description5')
#initialising ui
ux = UI(personController, activityController)
#running user interface
ux.mainMenu()
