import types

def greet(name):
    return "Hi!! "+name


sayHi=greet

print(sayHi("Rahul"))

def printType(param):
    print(type(param))

printType("Ramesh")
printType(True)
printType(353.53)
printType({1,3,5})
printType(sayHi)
print(isinstance(sayHi,types.FunctionType)) # error no type called function
print('##############')
print(callable(sayHi))

def funParam(fun): # callback function
    if(callable(fun)):
        for x in range(1,5):
            fun()
        
    else:
        print("pass only function as parameter")

def tap():
    print("Water")

funParam(12)
funParam(tap)

