class Animal:
    def __init__(self,animal_type,sound):
        self.animal_type=animal_type
        self.sound=sound

class Dog(Animal):
    def __init__(self,animal_type,sound,breed):
        super().__init__(animal_type,sound)
        self.breed=breed

dog=Dog("Dog","bark","husky")
animal=Animal("cat","meaw")
#print(isinstance(animal,dog)) #we cant use only object
print(isinstance(animal,Animal)) #  to check object is the instance of that class
print(isinstance(dog,Dog))
my_string="random string"
mylist=['a','b','c',1,2,3]
coplex=complex(3,4)
num=10
float1=2.5
print(isinstance(mylist,list)) #mylist is a list ----yes than  it return true
print(isinstance(my_string,str))
print(isinstance(coplex,complex))
print(isinstance(num,int))
print(isinstance(float1,float))
