class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __gt__(self,other):
        return self.age>other.age
    
    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":

    p1= Person('Raju',30)
    p2= Person('Vijay',20)
    p3= Person('Versha',21)

    if p1>p3:
        print(f'{p1.name} is elder')
    person_list=[p1,p2,p3]
    person_list.sort()
    print(person_list)

