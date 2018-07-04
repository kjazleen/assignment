f=open("text.txt","r")
print(f.read(10))#readlines(),
#print(f.tell())
f.seek(5,0)
print(f.tell())

'''f=open("text.txt","w")
l=['jazz\n','kaur']
f.writelines(l)
f.close()'''

#with open("text.txt","w") as f:
    #l=['jazleen\n','kaur']
   # f.writelines(l)