#Q1
r=int(input("enter radius"))
def area(r):
  return(3.14*r*r)
print(area(r))

#Q2
def perfect(p):
    sum=0
    for i in range(1,p):
        if(p%i==0):
            sum=sum+i
    if(sum==p):
        return True
    else:
        return False
for i in range(1,1001):
    if perfect(i):
        print(i)


#Q3
def table(n,t=1):
    if(t==11):
        return
    (print(str(n) + "x" + str(t) + "=" +str(n*t)))
    table(n,t+1)
table(n=12)

#Q4
a=int(input("enter a no. "))
b=int(input("enter its exponant value "))
def raise_to_power(a,b):
    if b==1:
        return a
    else:
        return(a*raise_to_power(a,b-1))
print('%d^%d=%d'%(a,b,raise_to_power(a,b)))

#Q5
def fact(f):
    if f==1:
        return 1

    g=(f*fact(f-1))
    return g
num=int(input("enter a no."))
h=fact(num)
d={num:h}
print(d)


