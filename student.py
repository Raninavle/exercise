class Student:
    Studentid=0
    def accept(self) :
        Student.Studentid+=1
        self.sname=input("Enter student name:")
        self.age=input("Enter a student age:")
        self.percent=float(input("Enter student percentage:"))

    def __init__(self,sname='studentname',age=18,per=35):
        Student.Studentid+=1
        self.sname=sname
        self.age=age
        self.percent=per

    def display(self):
        print("___________________________________-")
        print("student id :",Student.Studentid)
        print("student name:",self.sname)
        print("student age:",self.age)
        print("student percentage:",self.percent)

    def calrank(self):
        
        if(self.percent>=75):
            print("rank of student:","DISTINCTION")
        else:
            print("rank of student:","first class")
    
    def __str__(self):
        print("----------------------------------------------")
        data= "\nstudent id :"+str(Student.Studentid)
        data+="\nstudent name:"+str(self.sname)
        data+="\nstudent age:"+str(self.age)
        data+="\nstudent percentage:"+str(self.percent)
        return data


a=Student()
a.display()
a.accept()
a.calrank()
print(a)







      