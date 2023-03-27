
from student import Student
class Enggstudent(Student):
    def __init__(self,sname,age,per,branch='civil',intermrk=40):
        super().__init__(sname,age,per)
        
        self.branch=branch
        self.internalmrk=intermrk

    def display(self):
        super().display()
        print("student branch:",self.branch)
        print("student internalmarks:",self.internalmrk)

    def accept(self):
        self.branch =input("Enter a Branch:")
        self.internalmrk=int(input("Enter Internalmarks:"))


    def __str__(self):
        super().__str__()
        data="\nstudent branch:"+str(self.branch)
        data+="\nstudent internalmarks:"+str(self.internalmrk)
        return data

a1=Enggstudent('rani',24,89)
a1.display()


    


