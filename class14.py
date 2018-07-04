'''try:
    a=int(input("enter a no"))
    print(a)
    b=10/a

except(ValueError,ZeroDivisionError):
   print("please enter only integer")
else:
    print(b)
finally:
   print("i will execute whether exception occurs or not")'''

'''try:
     l=[1,2,3]
     print(l[3])
except IndexError:
    print("index is more than list element")'''

'''try:
    import sleep
    print("sleep")
except ImportError:
  print("there is an error")'''

class frustratedError(Exception):
    pass
try:
    a=int(input("enter a frustration level of me"))
    b=int(input("enter sm1 else level"))
    c=a+b
    if (c<10):
        raise frustratedError
except frustratedError:
    print("wrong pridiction")
except ValueError:
    print(c)