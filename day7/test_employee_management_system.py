from employee_management_system import Employee_management_system, Employee
import unittest
import sys

sys.path.append(r"C:\Users\Administrator\Desktop\valere labs\day6")


class TestEmps(unittest.TestCase):
    def setUp(self):
        self.manager = Employee_management_system()
        self.employe = Employee(1, "vidhi", 20, "manager", 20000, 4255322433)

    def tearDown(self):
        self.doCleanups()

    def test_add_employee(self):
        self.manager.add_employee()
        self.assertIn(self.employe.name, self.employe.name)
        self.assertEqual(self.employe.level, 'manager')

    def test_display_emp(self):
        self.manager.display_emp()
        self.assertTrue(Employee_management_system.employee == [])
        self.assertEqual(self.employe, Employee_management_system.employee)
        self.assertEqual(Employee_management_system.employee, [
                         1, 'vidhi', 20, 'manager', 20000, 53628791])

    def test_display_emp(self):
        self.assertTrue(Employee_management_system.employee > [])
        self.manager.display_emp()

    def remove(self):
        self.assertIn(Employee_management_system.employee.name, 'vidhi')
        self.manager.remove(self.name)

        self.assertFalse(Employee_management_system.employee.name == 'vidhi')

    def test_remove_all(self):
        self.manager.remove_all()
        self.assertTrue(Employee_management_system.employee == [])


if __name__ == "__main__":
    unittest.main()
