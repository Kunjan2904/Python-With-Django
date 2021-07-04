class myclass:
    def fun1(self):
        print('Hello')
    def fun2(self,name):
        print('Name is : '+name)
myc=myclass()
myc.fun1()
myc.fun2('Kunjan Patel')

# Sum of 2 number using class

class myclass:
    def fun1(self,n1,n2):
        ans = n1 + n2
        print('Ans is : ',ans)
myc=myclass()
myc.fun1(10,20)

'''There are two types of Constructor.
1.Default Constructor'''
class myclass:
    def __init__(self):
        print("Hello")
myc=myclass()

#2.Parameterized Constructo
class myclass:
    def __init__(self,name):
        print('Value is :',name)
myc=myclass('Kunjan Patel')

#Assign String Value to Class Variable Using Method

class myclass:
    name=""

    def fun1(self):
         print("Hello fun1")
    def fun2(self,name):
         self.name=name
    def fun3(self):
         print('Value is ',self.name)
myc=myclass()
myc.fun1()
myc.fun2("Kunjan Patel")
myc.fun3()

#Assign String Value to Class Variable Using constructor
class myclass:
    name=""

    def __init__(self,name):
        self.name=name

    def fun1(self):
        print('Name is :',self.name)
myc=myclass('Kunjan Patel')
myc.fun1()

#Inheritance

#1. Single level inheritance
class Parent:
     def __init__(self):
         print('Calling parent constructor')
     def parentmethod(self):
         print('Calling parent method ')

class Child(Parent):
    def __init__(self):
        print('Calling child constructor')
    def childmethod(self):
        print('Calling child method')

c=Child()
c.childmethod()
c.parentmethod()

#2. Multi level inheritance

class Parent:
    def __init__(self):
        print('Calling parent constructor')

    def parentmethod(self):
        print('Calling parent method ')

class Child(Parent):
    def __init__(self):
        print('Calling child constructor')

    def childmethod(self):
        print('Calling child method')

class Subchild(Child):
    def __init__(self):
        print('Calling sub child constructor')
    def subchildmethod(self):
        print('Calling sub child method')

sc = Subchild()
sc.subchildmethod()
sc.childmethod()
sc.parentmethod()

#3. Multiple Inheritance
class Parent1:
    def parent1_method(self):
        print('Parent1 method called')

class Parent2:
    def parent2_method(self):
        print('Parent2 method called')

class Child(Parent1,Parent2):
    def childmethod(self):
        print('Child method called')

c = Child()
c.parent1_method()
c.parent2_method()
c.childmethod()

#4. Hierarchical inheritance

class Parent:
    def __init__(self):
        print('Calling parent constructor')

    def parentmethod(self):
        print('Calling parent method ')


class Child(Parent):
    def __init__(self):
        print('Calling child constructor')

    def childmethod(self):
        print('Calling child method')

class Child2(Parent):
    def __init__(self):
        print('Calling child2 constructor')

    def childmethod2(self):
        print('Calling child2 method')

c = Child2()
c.childmethod2()
c.parentmethod()

'''5. Hybrid inheritance
Hybrid Inheritance is implemented by combining more than one
type of inheritance.'''

class Parent1:
    def parent1_method(self):
        print('Parent1 method called')

class Parent2:
    def parent2_method(self):
        print('Parent2 method called')

class Child(Parent1,Parent2):       # Multiple Inheritance
    def childmethod(self):
        print('Child method called')

class Childclass2(Parent1):         # Hierarchical Inheritance
    def childmethod2(self):
        print('Child2 method called')

c = Child()
c.parent1_method()
c.parent2_method()
c.childmethod()

c1 = Childclass2()
c1.childmethod2()
c1.parent1_method()

'''Polymorphism
Polymorphism is an ability (in OOP) to use common interface for
multiple form (data types).
Types of Polymorphism :-
1.Overriding Methods
2.Overloading Methods'''

#1.Overloading Methods

class Parent:

    def fun1(self):
        print('Parent class method called')

class Child(Parent):

    def fun1(self):
        print('Child class method called')

#object of child
c = Child()
c.fun1()

#object of parent
p = Parent()
p.fun1()

'''2.Overloading methods
Python does not supports method overloading.
We may overload the methods but can only use the latest defined
method.'''

class myclass():

    def sum(self,n1,n2):
        ans = n1+n2
        print('Sum is :',ans)

    def sum(self,n1,n2,n3):
        ans = n1+n2+n3
        print('Sum is :',ans)

p = myclass()
#p.sum(10,20)
p.sum(10,20,30)