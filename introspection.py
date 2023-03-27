#dir,id,type, __repr__, getattr, __doc__, __name__, __STR__
class Animal:
    def __init__(self,animal_type,sound):
        self.animal_type=animal_type
        self.sound=sound

    def print_attribute(self):
        print("animal attribute:",self.animal_type,self.sound)

    def __repr__(self):
        print("animal attribute:",self.animal_type,self.sound)

animal1=Animal("dog","bark")
animal2=Animal("dog","bark")
animal3=Animal("dog","bark")
print(id(animal1))
print(id(animal2))
print(id(animal3))
print(dir(Animal)) or print(dir(animal1))
num=10
print(dir(num))
print(hasattr(Animal,"print_attribute")) #yes true
print(hasattr(animal1,"print_attribute"))
print(getattr(animal1,"sound")) #use object to getattr
print(animal1)