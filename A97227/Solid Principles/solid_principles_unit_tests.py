#Refactored Code 

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_bonus(self):
        pass

    @abstractmethod
    def get_report(self):
        pass

class Manager(Employee):
    def get_bonus(self):
        return 1000

    def get_report(self):
        return f"Manager Report: {self.name}"

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def get_bonus(self):
        return 500

    def get_report(self):
        return f"Developer Report: {self.name}"

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

class BonusCalculator:
    def calculate_bonus(self, employee: Employee):
        return employee.get_bonus()

class ReportGenerator:
    def generate_report(self, employee: Employee):
        print(employee.get_report())

if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()


#Unit Test Code

import unittest
from io import StringIO
import sys

# Assuming the above classes are defined in a module named elevate_hr

class TestElevateHR(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_employee_creation(self):
        manager = Manager("Alice")
        developer = Developer("Bob")
        self.assertEqual(manager.name, "Alice")
        self.assertEqual(developer.name, "Bob")

    def test_bonus_calculation(self):
        manager = Manager("Alice")
        developer = Developer("Bob")
        bonus_calculator = BonusCalculator()
        self.assertEqual(bonus_calculator.calculate_bonus(manager), 1000)
        self.assertEqual(bonus_calculator.calculate_bonus(developer), 500)

    def test_report_generation(self):
        manager = Manager("Alice")
        developer = Developer("Bob")
        report_generator = ReportGenerator()
        report_generator.generate_report(manager)
        self.assertIn("Manager Report: Alice", sys.stdout.getvalue())
        sys.stdout.seek(0)  # Reset the stdout buffer
        report_generator.generate_report(developer)
        self.assertIn("Developer Report: Bob", sys.stdout.getvalue())

    def test_specific_methods(self):
        manager = Manager("Alice")
        developer = Developer("Bob")
        manager.manage_team()
        self.assertIn("Alice is managing the team.", sys.stdout.getvalue())
        sys.stdout.seek(0)  # Reset the stdout buffer
        developer.code_review()
        self.assertIn("Bob is conducting a code review.", sys.stdout.getvalue())

    def tearDown(self):
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()
