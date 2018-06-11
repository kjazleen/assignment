#Q1 check if it is leap year or not
y=int(input("enter a year "))
if(y%4==0):
    print("this year is a leap year")
else:
    print("this year is not a leap year")

#Q2 check if the dimensions are of square or are of rectangle
l=int(input("length="))
b=int(input("breadth="))
if(l==b):
    print("its a square")
else:
    print("its a reactangle")

#Q3 determine who is the youngest and who is oldest
i=int(input("enter the age of first person i="))
j=int(input("enter the age of second person j="))
k=int(input("enter the age of third person k="))
if(i>j and i>k):
    print("i is the oldest person")
elif(j>i and j>k):
    print("j is the oldest person")
elif(k>i and k>j):
    print("k is d oldest person")
else:
    print("other are of same age")
if(i<j and i<k):
    print("i is the youngest person")
elif(j<i and j<k):
    print("j is the youngest person")
elif(k<i and k<j):
    print("k is the youngest person")
else:
    print("other are of same age")

#Q4 prizes on the basis of points
p=int(input("enter the no. pf points scored="))
if(p<=50):
    print("no prize")
elif(p<=150):
    print("wooden dog")
elif(p<=180):
    print("book")
elif(p<=200):
    print("chocolates")

#Q5 print cost after discount if purchased quantity is more dn 1000
q=int(input("quantity="))
r=q*100
if(r>1000):
    print("discount is there"+str(r-0.10*q*100))
else:
    print((q)*100)






