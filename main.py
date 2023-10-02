from person import Person
from employee import Employee
from customer import Customer
from regular_customer import RegularCustomer

if __name__ == '__main__':
    # eine allgemeine Person erstellen
    person = Person('Max', 25)
    person.address = 'Musterdorf'
    person.print()
    print("--------------------------------------------")
    # Einen Mitarbeiter erstellen
    employee = Employee('Joel', 35, '723-123', '01 03 04 05')
    employee.address = 'Weltdorf'
    employee.salary = 6000.00
    employee.print()
    print("--------------------------------------------")
    # einen Kunden erstellen
    customer = Customer('Moritz', 45, employee)
    customer.address = 'Oberdorf'
    customer.print()
    print("--------------------------------------------")
    # eine Stammkundin erstellen
    regular = RegularCustomer('Pia', 25, employee)
    regular.address = 'Oberdorf'
    regular.discount = 2.4
    regular.print()
    print("--------------------------------------------")