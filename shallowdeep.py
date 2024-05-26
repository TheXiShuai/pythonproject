#deep copy

# import copy

# things = ["working out", 7, ['prime', 'netflix']]

# c = copy.deepcopy(things)

# c[2][0] = "HBO"

# print(c, things)


import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Paul', 25)

company = Company(p1,p2)
# SHALLOW COPY
company_clone = copy.copy(company)
# DEEP COPY
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


    
    



