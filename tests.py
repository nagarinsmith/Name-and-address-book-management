import datetime
from unittest import TestCase

import os

from domain import Person, Activity
from repository import Repository, PickleRepository
from service import PersonService, ActivityService


class Tests(TestCase):
    def testPerson(self):
        p = Person(1, "blabla", "0756144243", "Address 12 42 42 42")
        p.Id = 1
        self.assertEqual(p.Id, 1, "Id error")
        p.name = "blabla"
        self.assertEqual(p.name, "blabla", "name error")
        p.phoneNumber = "0756144243"
        self.assertEqual(p.phoneNumber, "0756144243", "phoneNumber error")
        p.address = "Address 12 42 42 42"
        self.assertEqual(p.address, "Address 12 42 42 42", "address error")
        self.assertEqual(p, p, "equality error")
        self.assertFalse(p == 1, "equality error")
        self.assertEqual(str(p), "Id: 1, Name: blabla, Phone Number: 0756144243, Address: Address 12 42 42 42")

    def testActivity(self):
        a = Activity(1, 1, datetime.date(2018, 5, 3), datetime.time(13, 30), "Descr")
        a.Id = 1
        self.assertEqual(a.Id, 1)
        a.personIds = [1]
        self.assertEqual(a.personIds, [1])
        a.date = datetime.date(2018, 5, 3)
        self.assertEqual(a.date, datetime.date(2018, 5, 3))
        a.time = datetime.time(13, 30)
        self.assertEqual(a.time, datetime.time(13, 30))
        a.description = "Descr"
        self.assertEqual(a.description, "Descr")
        self.assertEqual(a, a)
        self.assertFalse(a == 1)
        self.assertEqual(str(a), "Id: 1, Person Ids: 1, Date: 2018-05-03, Time: 13:30:00, Description: Descr")

    def testRepository(self):
        repo = Repository()
        repo.store(Person(14, "Nume", "0745616223", "Adresa"))
        self.assertEqual(repo.find(14), Person(14, "Nume", "0745616223", "Adresa"))
        repo.delete(14)
        self.assertEqual(repo.find(14), None)
        repo.store(Person(14, "Nume", "0745616223", "Adresa"))
        self.assertEqual(repo.find(14).name, "Nume")
        repo.update(Person(14, "Numenume", "0745616223", "Adresa"))
        self.assertEqual(repo.find(14).name, "Numenume")
        repo.store(Person(15, "Nume", "0745616223", "Adresa"))
        self.assertEqual(repo.getAll(),
                         [Person(14, "Numenume", "0745616223", "Adresa"), Person(15, "Nume", "0745616223", "Adresa")])
        self.assertIsNotNone(str(repo))
        pickleRepo = PickleRepository()
        os.remove('repo.pickle')
        f = open("repo.pickle", "w+")
        f.close()
        pickleRepo.store(Person(14, "Nume", "0745616223", "Adresa"))
        self.assertEqual(pickleRepo.find(14), Person(14, "Nume", "0745616223", "Adresa"))
        pickleRepo.delete(14)
        self.assertEqual(pickleRepo.find(14), None)
        pickleRepo.store(Person(14, "Nume", "0745616223", "Adresa"))
        self.assertEqual(pickleRepo.find(14).name, "Nume")
        pickleRepo.update(Person(14, "Numenume", "0745616223", "Adresa"))
        self.assertEqual(pickleRepo.find(14).name, "Numenume")
        pickleRepo.store(Person(15, "Nume", "0745616223", "Adresa"))
        self.assertEqual(pickleRepo.getAll(),
                         [Person(14, "Numenume", "0745616223", "Adresa"), Person(15, "Nume", "0745616223", "Adresa")])
        self.assertEqual(len(pickleRepo), 2)
        self.assertIsNotNone(str(pickleRepo))

    def testService(self):
        activityRepo = Repository()
        personRepo = Repository()
        personService = PersonService(activityRepo, personRepo)
        personService.create(14, "Nume", "0745616223", "Adresa")
        self.assertEqual(personRepo.find(14), Person(14, "Nume", "0745616223", "Adresa"))
        personService.delete(14)
        self.assertEqual(personRepo.find(14), None)
        personService.create(14, "Nume", "0745616223", "Adresa")
        self.assertEqual(personRepo.find(14).name, "Nume")
        personService.update(14, "Numenume", "0745616223", "Adresa")
        self.assertEqual(personRepo.find(14).name, "Numenume")
        self.assertEqual(str(personService.list()),
                         "\nId: 14, Name: Numenume, Phone Number: 0745616223, Address: Adresa\n")
        self.assertIsNotNone(str(personService.search(1, "Nume")))
        activityService = ActivityService(activityRepo, personRepo)
        activityService.create(1, [14], datetime.date(2018, 1, 1), datetime.time(0, 0), "descr")
        self.assertIsNotNone(activityService.list())
        self.assertIsNotNone(activityService.dayOfWeekActivities(1))
        self.assertIsNotNone(activityService.busiestDays())
        self.assertIsNotNone(activityService.activitiesWithPerson(14))
        self.assertIsNotNone(activityService.sortedPersons())
        activityService.update(1, [14], datetime.date(2018, 1, 1), datetime.time(0, 1), "descr1")
