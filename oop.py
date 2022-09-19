class Emp:
    def __init__(self,eno,name,city): #dunder methods -double underscore - magic methods
        self.eno=eno
        self.name=name
        self.city=city
    
    def __str__(self):
             return str( {
            'sno': self.eno,
            'name': self.name,
            'city':self.city
        })

    def show(self):
        print('eno::',self.eno)
        print('name::',self.name)
        print('city::',self.city)

emp1=Emp(1,'Raj','Chennai')
emp2=Emp(2,'Ram','Mumbai')

emp1.show()
emp2.show()

print(emp1)
print(emp2)