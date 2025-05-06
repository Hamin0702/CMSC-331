# Hamin Han XK26538

# Q1
import re

q1 = "ABCD+++1234+EFGH++****"

result = re.sub('\++', '-', q1)
print(result) # prints ABCD-1234-EFGH-****

# Q2
q2 = [x*2 if x%2 == 0 else x**2 for x in range(1,31)]
print(len(q2), 'numbers in q2 list')
print(q2)

# Q3
str_list = ['UMBC', 'UMD', 'UMB', 'TU']

q3 = filter(lambda x: len(x) >= 4, str_list)

print(type(q3))
print(list(q3))

# Q4
# Vehicle class
class Vehicle:

    def __init__(self, initMake, initModel, initYear):

        self.make = initMake
        self.model = initModel
        self.year = initYear

    def isNew(self):

        return self.year == 2021


q4 = Vehicle('Honda', 'Accord', 2021)
print(type(q4))
print(q4.__dict__)
print(Vehicle.isNew(q4))

# Q5
# SUV class
class SUV(Vehicle):

    def __init__(self, initTransmission, initMilage, *args, **kwargs):

        self.transmission = initTransmission
        self.milage = initMilage
        super().__init__(*args, **kwargs)

q5 = SUV('Automatic', 75000, 'Honda', 'CRV', 2020)
print(type(q5))
print(q5.__dict__)
print(SUV.isNew(q5))