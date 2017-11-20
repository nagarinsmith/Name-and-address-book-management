
from repository.repository import Repository
from domain.activity import Activity
from domain.person import Person

activitiRepo = Repository()
personRepo = Repository()

activitiRepo.add(Activity(1, [1], '18 Nov 2017', '00:00', 'Sample description'))

personRepo.add(Person(1, 'Paul Orha', '0745616223', 'Str. George Cosbuc 35/46, Baia Mare, Romania'))

