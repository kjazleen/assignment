#Q1
'''class Animal:
    def animal_attribute(self):
        print("this animal has four legs")
class Tiger(Animal):
    def animal_type(self):
        print("its a carnivore")
x=Tiger()
x.animal_attribute()'''


#Q2 result:
#AB
#AB

#Q3
class Cop:
    def __init__(self,name,age,work_experience,designation):
        self.name=name
        self.age=age
        self.work_experience=work_experience
        self.designation=designation
    def display(self):
        print("display information before updation")
        print("name ",self.name)
        print("age ",self.age)
        print("work_experience",self.work_experience)
    def _update_(self,name,age,work_experience,designation):
        self.name=name
        self.age=age
        self.work_experience=work_experience
        self.designation=designation
class Mission(Cop):
    def add_mission_details(self,name,age,work_experience,designation):
        print("updated information")
        print("name:")
        self.name=name
        print(name)
        print("age:")
        self.age=age
        print(age)
        print("work experience:")
        self.work_experience=work_experience
        print(work_experience)
        print("designation:")
        self.designation=designation
        print(designation)
m=Mission("jasleen",20,8,"singer",)
name=input("enter ur name ")
age=int(input("enter ur age "))
work_experience=int(input("enter ur work_experience "))
designation=input("enter ur designation ")
m.display()
n=Mission(name,age,work_experience,designation)
n.add_mission_details(name,age,work_experience,designation)





#Q4
'''class Shape:
   def __init__(self,length,breadth):
       self.length=length
       self.breadth=breadth
class Rectangle(Shape):
    def area(self):
        area=(self.length*self.breadth)
        print("area of rectangle is ")
        print(area)
class Square(Shape):
    def area(self):
        area=(self.length*self.breadth)
        print("area of square is ")
        print(area)
r=Rectangle(2,4)
s=Square(4,4)
r.area()
s.area()'''




