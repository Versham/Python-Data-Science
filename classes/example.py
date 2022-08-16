class Dog:
    def __init__(self,breed,color,age):
        #instance variables
        self.breed = breed
        self.color = color
        self.age = age

    def bark(self,count=3):
        print("woof"*count)

    def eat(self,food):
        print(f"dog eats {food}")

    
class Shape:

    def __init__(self,name,sides):
        self.name = name
        self.sides = sides

    def perimeter(self,size=20):
        return self.sides*size

    #string notation of the object
    def __str__(self):
        return f"{self.name} has {self.sides} sides"


#this line checks if the file you ran is this file or not
if __name__ == "__main__":
    tommy = Dog('Street Dog', 'black', 3)
    tiger = Dog('Bulldog','brown',2)

    print('object',tommy)
    print('object',tiger)

    print('tommy\'s breed',tommy.breed)
    print('tommy\'s age',tommy.age)

    print('tiger\'s breed',tiger.breed)
    print('tiger\'s age',tiger.age)

    sqr = Shape('square',4)
    tri = Shape('triangle',3)
    pet = Shape('pentagon',5)

    print('object=>', sqr)
    print('object=>',tri)
    print('object=>', pet)

    print("square perimeter", sqr.perimeter())
    print("triangle perimeter", tri.perimeter(300))
    print("pentagon perimeter", pet.perimeter(20))