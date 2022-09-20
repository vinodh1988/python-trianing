class CallableNotAllowed(Exception):
    def __init__(self,message):
        self.message=message
    
    def __repr__(self):
        return self.message
def printCollection(a):
    try:
        for x in a:
            if(callable(x)): 
                raise(CallableNotAllowed('\nthis is a function - Error'))
            print(int(x),end=" -> ")
    except TypeError as a:
        print('\nit is not iterable')
    except ValueError as a:
        print('\n it is a value error')
    except CallableNotAllowed as a:
        print(a)
    except:
        print("\nSome exception occured")
    else:
        print('\n This will get called only when there is no exception')
    finally:
        print('\n regardless of exception finally runs always')
    print('-------------------------------------------------------------')
   
#printCollection({1,3,35})
#printCollection((1,3535,36345,34))
#printCollection(155)
#printCollection([3,35,53])
#printCollection(13)
printCollection([1,2,lambda x:x*x])

print('After code')