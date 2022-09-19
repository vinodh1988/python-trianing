a=[12,34,546,46,46,677] #list is  collection of objects 
                        # list is mutable 
                        # list is ordered [order of insertion]
                        # list is indexed

a.insert(3,34536)

print(a)

print(a[3])
print(a[1:5])
print(a[1:6:2]) # in step of 2

print(a[::-1])
print(a[-1:-5:-1])

b=(1,2,536,34) #Immutable - tuple of
               # same as list but cannot be changed[immutable]

print(b)
print(b[2])

c= {1,35,56,35,647,23,266,23} # set wont allow duplicates
                              # set is not ordered and not indexed

c.add(50)

print(c)

#print(c[3])

for x in c:
    print(x)