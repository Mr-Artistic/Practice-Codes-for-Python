# For exercise 11-1 and 11-2

from Module_City_Functions import neat_city
from Module_Employee import Employee

def test_neat_city_function():
    """Tests the city country function"""
    test = neat_city('Pune', 'India', population=10_00_00_000)
    assert test == 'Pune, India, population: 100000000'

# For exercise 11-3

def test_give_raise_function():

    samad = Employee('Samad', 'Mughal', 35_000)
    samad.give_raise()
    assert samad.salary == 40_000

    sumiet = Employee('Sumiet', 'Talekar', 35_000)
    sumiet.give_raise(10_000)
    assert sumiet.salary == 45_000

import pytest

@pytest.fixture
def employee_instance():
    """An employee class instance for testing"""
    return Employee('Test_First_Name', 'Test_Last_Name', 35_000)

def test_default_raise_function(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.salary == 40_000
    employee_instance.give_raise(10_000)
    assert employee_instance.salary == 50_000

def test_describe_employee(employee_instance):
    employee_instance.describe_employee()
    assert employee_instance.firstname == 'Test_First_Name'
    assert employee_instance.lastname == 'Test_Last_Name'



