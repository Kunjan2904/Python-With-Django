#Input/Outiput Functions

n1 = input ('Enter a Number: ')
print("Value is:",n1)

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
ans=n1+n2
print(ans)

#Conditional Statements

#if Statements
x=10
y=20
if x > y:
    print('x is a greater number')

if y > x:
    print('y is a greater number')

#if... else Statement
x=20
y=10
if x > y:
    print('x is a greater number')
else:
    print('y is a greater number')

#if ...elif...else Statement
x=20
y=10
if x == y:
    print("Both values are equal")
elif x > y:
    print('x is a greater number')
else:
    print('y is a greater number')


#Nested if Statements
x=20
if x >= 20:
    if x == 0:
        print("zero")
    else:
        print('x is a positive number')
else:
    print('x is a negative number')

#Loops

#while loop
i=0
while i < 5:
    print("value of i : ",i)
    i += 1

#for loop
for i in 'Hello':
    print('value :', i)

#Example With List Datatype
list1=[10,20,'Kunjan Patel']

for i in list1:
    print('value :', i)

#range Function
for x in range(5):
    print('First range : ',x)

for y in range(3,6):
    print('Second range : ',y)

for z in range(1,5,2):
    print('Third range : ',z)

#Example 2
list1=[10,20,'Kunjan Patel']
for i in range(len(list1)):
    print('Value is :', list1[i])

#loop with else
list1=[10,20,'Kunjan Patel']
for i in range(len(list1)):
    print('Value is :', list1[i])
else:
    print('No elements Left')

# break and continue Statements
    #Example of break Statement
i=0
while i < 10:
    print("Value is : ",i)
    i += 1
    if i >= 5:
        break

#Example of continue Statement

for i in range(10):
    if i % 2 == 0:      # check if x is even
         continue
    print("Value is :",i)

#pass Statement :

while i < 5:
    pass

