#!/usr/bin/env python3

class Employee:
    def computeSalary(self): ...
    def giveRaise(self): ...
    def promote(self): ...
    def retire(self): ...

class Engineer(Employee):
    def computeSalary(self): ...

bob = Employee()
sue = Employee()
tom = Engineer()

company = [bob, sue, tom]

from emp in company:
        print(emp.computeSalary())
