lista=[34,35,5,3646,45,45,6,45,64,6,1345,124,56,45,46,64,33,366,123,555,122,331]

#filter carries two parameters one is 
# list 
# a function which returns boolean 
# filter returns a collection which only contains the values that returns true for callback
def filterfun(a):
    if(a>=100 and a<=999):
        if(a%2==0 and a%3==0):
            return True
        return False
    return False


divby3=filter(lambda x: True if x%3==0 else False,lista)
even=filter(lambda x: True if x%2==0 else False,lista)
numberendswith3=filter(lambda x:True if x%10==3 else False,lista)
n23andthreeddigit=filter(filterfun,lista)

print(list( divby3))
print(list(even))
print(list(numberendswith3))
print(list(n23andthreeddigit))