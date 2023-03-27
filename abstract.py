# abstract method ,abstrct method have no finction body,
#we cant create the object of abtrct class,
#and abstarct class must have one abstrct method
#but we can inherite the abstrct class with child class and overlode the method in child class
from abc import ABC,abstractmethod 
class Shape(ABC):
    @abstractmethod
    def has_shape(self):
        pass

    @abstractmethod
    def cal_area(self):
        pass

class circle(Shape):
    def __init__(self,redius):
        self.redius=redius

    def has_shape(self):
        print("shape of cirle")

    def cal_area(self):
        print("area of circle:",3.14*self.redius*self.redius)

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def has_shape(self):
        print("shape of rectangle")

    def cal_area(self):
        print("area of circle:",self.length*self.width)

#shape=Shape() we cant crete the object of abstarct class
cricle=circle(10)
rect=Rectangle(3,4)
cricle.cal_area()
cricle.has_shape()
rect.cal_area()
rect.has_shape()