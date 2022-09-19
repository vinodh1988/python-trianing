def optional(a=10,b=30,c=50):
    print(a,b,c)

#def champ(a=10,b): error
#   print(a,b)

optional(12,35,53)
optional(35)
optional(35,36)
optional(c=90)
optional(c=10,a=15)

#champ(30)
# functions with variable number of parameters
def parameters(*a):
    print(a)
    for x in a:
        print(x,end=" ")

parameters(1,2)
print("\n-----------------")
parameters(3,536,436,45,3)

#function with variable no of parameters and named parameters

print('\n##########################')
def namecumvar(*a,**b): 
    print(a)
    print(b)

namecumvar(1,2,3)
namecumvar(353,6345,sno=1,name='Ravi',city='Mumbai')
namecumvar(sno=1,name='Raj')
#namecumvar(sno=1,name='Rahul',24) error - named parameters must be right

