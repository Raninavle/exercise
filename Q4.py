m1=float(input("Enter marks obtained in Marathi:"))
m2=float(input("Enter marks obtained in Hindi:"))
m3=float(input("Enter marks obtained in English:"))
m4=float(input("Enter marks obtained in Science:"))
m5=float(input("Enter marks obtained in History:"))
avg=((m1+m2+m3+m4+m5)/5)
print("average marks:",avg)
if(avg>=90):
    print("Grade A")
elif(avg>=80):
    print("Grade B")    
elif(avg>=70):
    print("Grade C")  
elif(avg>=60):
    print("Grade D")    
elif(avg>=50):
    print("Grade E")
elif(avg<40):
    print("Grade F")
else:
    print("Fail")





  