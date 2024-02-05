from abc import ABC, abstractmethod

# Abstract base class for Employee, adhering to ISP
class Employee(ABC):
    def __init__(self, name):
        """Initialize an Employee with a name."""
        self.name = name

    @abstractmethod
    def get_bonus(self):
        """Abstract method to get the bonus for an Employee."""
        pass

    @abstractmethod
    def get_report(self):
        """Abstract method to get a report for an Employee."""
        pass

# Concrete implementations for Manager and Developer, adhering to OCP and SRP
class Manager(Employee):
    def get_bonus(self):
        """Get bonus for a Manager."""
        return 1000

    def get_report(self):
        """Generate a report for a Manager."""
        return f"Manager Report: {self.name}"

    def manage_team(self):
        """Manager-specific action to manage a team."""
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def get_bonus(self):
        """Get bonus for a Developer."""
        return 500

    def get_report(self):
        """Generate a report for a Developer."""
        return f"Developer Report: {self.name}"

    def code_review(self):
        """Developer-specific action to conduct a code review."""
        print(f"{self.name} is conducting a code review.")

# BonusCalculator now depends on the abstraction, adhering to DIP
class BonusCalculator:
    def calculate_bonus(self, employee: Employee):
        """Calculate bonus for an Employee using the Employee abstraction."""
        return employee.get_bonus()

# ReportGenerator also depends on the abstraction, adhering to DIP
class ReportGenerator:
    def generate_report(self, employee: Employee):
        """Generate a report for an Employee using the Employee abstraction."""
        report = employee.get_report()
        print(report)

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
