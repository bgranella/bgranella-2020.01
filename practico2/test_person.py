import unittest
from employee import Person


class TestPerson(unittest.TestCase):
    def test_get_person(self):
        persona1 = Person("Bautista", 23)
        print(Person.get_person(persona1))
        self.assertEqual(Person.get_person(persona1), ["Bautista", 23])


if __name__ == '__main__':
    unittest.main()