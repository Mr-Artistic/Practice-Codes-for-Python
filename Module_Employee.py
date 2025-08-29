class Employee:
    def __init__(self, first_name, last_name, the_salary):
        """Initialize an Employee object to hold information about employee."""
        self.firstname = first_name
        self.lastname = last_name
        self.salary = the_salary

    def give_raise(self, raise_amount=5_000):
        self.salary += raise_amount

    def describe_employee(self):
        print(f"Employee Name: {self.firstname} {self.lastname}")


E001 = Employee('Sumiet', 'Talekar', 35_000)
E001.give_raise(10_000)
print(E001.salary)

