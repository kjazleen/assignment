t=(1,2,3)
print(t)
del t
print(t)
a=[1,2,3]
b=tuple(a)
print(b)
a=[1,2,3]
str=str(a)
print(str)
a=(1,2,3)
print(min(a))
a=(1,2,3)
b=(4,5,6)
print(cmp(a,b))
s=set([1,2,3])
p=set([3,5,6])
r=s&p
print(r)
s=set((1,2,3))
s.add(4)
print(s)
s=set([1,2,3])
s.discard(2)
print(s)
s=set([1,2,3,4,5])
p=set([2,3,5])
r=s>=p
print(r)
d={"name":"jasleen","science":80,"maths":80,"english":85}
del d
print(d)

