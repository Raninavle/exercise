from distutils.spawn import spawn
from student import Student

class Medicalstudent(Student):
    def __init__(self,sp,mrk):
        super().__init__()
        self.specilization=sp 
        self.mrkofintership=mrk

    
