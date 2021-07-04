#Function

def myfunction():
    print("Kunjan Patel")
myfunction()
myfunction()

#Example with argument
def myfunction(name):
    print("Name is :",name)
myfunction("Kunjan")

#Example with return statement
def myfunction(name):
    return name
name=myfunction('Kunjan Patel')
print(name)

#Example with multiple return statement
def myfunction():
    name="Kunjan"
    x=20
    return name,x
name,x = myfunction()
print("Name is :",name)
print("x is:",x)

'''python arguments
* Three types of argument
1. default argument
2. keyword argument
3. variable length'''

#default argument
def sum(a=8,b=6):
    print(a+b)
sum(10,20)
sum()

#keyword argument
def sum(a,b):
    print("Sum is :",a+b)
sum(b=20,a=10)

'''variable length argument
 1. Non keyword argument(*)'''
def sum(*n1):
    sum=0

    for i in n1:
        sum = sum + i

    print('Sum is :',sum)

sum(10,20)
sum(10,20,30)

# 2. Keyword argument(**)
def myfunction(**arg):
    for i,j in arg.items():
        print(i,j)

myfunction(name='Kunjan',age=18)

'''scope of variable
1.local
2.global '''

def myfun():
    x=10
    print('Value inside function:',x)
y=20
myfun()
print('Value outside function:',y)

#operators
#1. Arithmetic

a=10
b=9
print('a + b =',a+b)
print('a - b =',a-b)
print('a * b =',a*b)
print('a / b =',a/b)
print('a // b =',a//b)
print('a ** b =',a**b)

#2. Comparison
a=10
b=9
print('a < b =',a<b)
print('a > b =',a>b)
print('a <= b =',a<=b)
print('a >= b =',a>=b)
print('a != b =',a!=b)
print('a == b =',a==b)

#3. logical
#AND
a=10
b=20
c=30
if a > b and a > c:
    print('a is largest number ')
if b > a and b > c:
    print('b is greatest number')
if c > a and c > b:
    print('c is greatest number')

#OR
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

#4. Membership operator

a=10
b=9
list1=[10,20,50,60]

print(a in list1)
print(b in list1)
print(b not in list1)

#5. identity operator

x=30
y=30

print(x is y)

print(x is not y)
