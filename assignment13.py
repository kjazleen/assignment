#Q1
try:
    a=3
    if a<4:
      a=a/(a-3)
      print(a)
except(ValueError,ZeroDivisionError):
    print("enter only integer and should not b zero")


#Q2
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("enter correct index value")

#Q3
#an exception

#Q4
#-5.0
#a/b result in 0

#Q5
#IMPORT ERROR
try:
    import lushlife
except ImportError:
    print("enter defined import function")
#HANDLING
try:
    import threading
except ValueError:
    print("enter defined import function")

#VALUE ERROR
try:
    a=int(input("enter a no."))
except IndexError:
    print("enter a integer number")

 #INDEX ERROR
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("enter valid index ")
 #HANDLING
try:
    l=[1,2,3]
    print(l[2])
except ImdexError:
    print("enter valid index")

#Q6
class AgeTooSmall(Exception):
    pass
a=True
while(a):
    try:
        age=int(input("enter age"))
        if(age>=18):
            a=False
            raise AgeTooSmall
        else:
            print(age)
    except AgeTooSmall:
        print("age is greater than 18")
    except ValueError:
        print("enter an integer value")