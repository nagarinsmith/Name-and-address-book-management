import datetime
from unittest import TestCase
from domain import Person, Activity


class TestPerson(TestCase):
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
