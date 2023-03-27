class Animal:
    def __init__(self,animal_type,sound):
        self.animal_type=animal_type
        self.sound=sound

class Dog(Animal):
    def __init__(self,animal_type,sound,breed):
        super().__init__(animal_type,sound)
        self.breed=breed

class stratdog(Dog):
    def __init__(self,animal_type,sound,breed):
        super().__init__(animal_type,sound,breed)

class person():
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

dog=Dog("Dog","bark","husky")
animal=Animal("cat","meaw")
print(issubclass(Dog,Animal)) #(childclass,prentclass) true
print(issubclass(Animal,Dog))#false
print(Dog,person)#false