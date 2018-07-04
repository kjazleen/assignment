#Q1
'''f=open("text.txt",encoding="utf8")
j=(f.readlines())
j.reverse()
n=int(input("enter a no. of line you want to choose"))
for i in range(0,n):
    print(j[i])'''

#Q2
'''a="best"
f=open("text2.txt",'r')
b=f.read()
c=b.split()
print(b.count(a))'''

#Q3
'''f=open("text.txt",encoding="utf8")
f1=open("textcopy.txt","w")
for story in f:
 f1.write(story)
f.close()'''

#Q4
'''i=0
f=open("text.txt",encoding="utf8")
x=(f.readlines())
f1=open("text1.txt","r")
y=(f1.readlines())
f3=open("text3.txt","w")
for i,j in zip(x,y):
    f3.write(i+j)
f.close()
f1.close()
f3.close()'''

#Q5
import random
list=[]
for i in range(10):
    a=list.append(random.randint(1,10))
    print(list)
    











