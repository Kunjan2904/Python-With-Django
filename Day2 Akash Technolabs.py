#Comment in Python

        #In Python, we use the hash (#) symbol to start writing a comment

# print("Hello Word")    //single line comment


''' This is a multi     //this is a multiline Comment(Use Three Quotes)
        line
        comment'''

# Variable in pyhon
    #How to declare and use a variable

a=20
b="Kunjan Patel"
c=19.6

print(a)
print("name is:",b)
print("value of c is:",c)

#changing value of variable
name="Kunjan"
print("Name is:",name)

name="Kunjan Patel"
print("Name is:",name)

#Assigning multiple values to multiple variables

a,b,c=15,19.5,"Kunjan Patel"

print(a)
print("value of b is:",b)
print("name is:",c)

#Assign the same value to multiple variables

x = y = z = 10
print("value of x is:",x)
print("value of y is:",y)
print("value of z is:",z)

#Data type in python

#1.Numeric
n1=15
print(n1,"is of type",type(n1))
n2=13.5
print(n2,"is complex number?",isinstance(13.5,int))
n3=2+1j
print(n3,"is complex number?",isinstance(2+1j,complex))

#2.String

a="Kunjan Patel"
print("name is:",a)   #print complete string
print(a[0])           #print first character of string
print(a[3:7])         #print character starting from 3 to 7
print(a[3:])          #print string starting from 3 character
print(a * 2)          #print string two times
print(name+ "Hello")  #print concatenated string

#3.List

list1=[19,12.5,"Kunjan",25,50,40,"Patel"]
print(list1)
print("list1[2] = ",list1[2])
print("list1[0:4] = ",list1[0:4])
print("list1[4:] = ",list1[4:])

# Take values from the user
lst=[]
n=int(input('Enter number of elements : '))
for i in range(0,n):
    ele = input("Enter Value: ")
    lst.append(ele)
print(lst)


#3.Tuple

tuple1=(19,12.5,"Kunjan",25,50,40,"Patel")
print(tuple1)
print("tuple1[2] = ",tuple1[2])
print("tuple1[0:4] = ",tuple1[0:4])
print("tuple1[4:] = ",tuple1[4:])

#we are changing value of tuple will generate error
#tuple1[3]=30
#print(tuple1)

# Take values from the user
lst=[]
n=int(input('Enter number of elements : '))
for i in range(0,n):
    ele = input("Enter Value: ")
    lst.append(ele)
tup1=tuple(lst)
print(lst)
print(tup1)

#4.dictionary

d={1:'Kunjan',2:'Patel','key':15}
print(type(d))
print("d[1]=",d[1])
print("d[2]=",d[2])
print("d['key']=",d['key'])
