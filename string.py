s=input("Enter string :")#rani135
count=0
for i in s:
    if(i in 'aeiou'):
        #print(i)
        count+=1
print("vowels",count)
v=0
for i in s:
    if(i.isdigit()):
        v+=1
print("NUmber:",v)
print("-------------------------------")

result=""
s=input("Enter string:")
for i in s:
    if(i.isalpha()):
        ch=ord(i)+1
        ch=chr(ch)
        if(ch in "aeiou"):
            result+=ch.upper()
        else:
            result+=ch
    else:
        result+=i
print(result) 

#reverse string:
s="first"
m=" "
for x in s:
    m= x+ m
print(m)