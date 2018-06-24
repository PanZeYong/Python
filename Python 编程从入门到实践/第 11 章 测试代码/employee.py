class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.annual_salary = 5000

    def give_raise(self, annual_salary=5000):
        self.annual_salary += annual_salary
        return self.annual_salary
