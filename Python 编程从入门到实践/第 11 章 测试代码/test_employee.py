import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Julian', 'Pan')

    def test_give_default_raise(self):
        salary = self.employee.give_raise()
        self.assertEqual(10000, salary)

    def test_give_custom_raise(self):
        salary = self.employee.give_raise(10000)
        self.assertEqual(15000, salary)

unittest.main()
