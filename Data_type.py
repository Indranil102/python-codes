a=1
b=1.0
c=1+2j
print(type(a))
print(type(b))
print(type(c))
s='whatupp'
print(type(s))
k='10'
print(type(k))

#list
lst=[10,2.2,'wow']
lst[1]=5.6    # list is mutalbe it can upadate its value
print(lst)

#tuple
t=('a',10,50.236)
print(t,type(t))   #it is immutable

#dictionary
d={'name':"jaypee university",
   "branch":"CSE"}

print(d['name'])
print(d,type(d))


#set
se={1,2,3,4,51,1}
print(se,type(se))   #set is immutable and every value in set is unique