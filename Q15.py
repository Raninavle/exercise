num=int(input("Enter your amount:"))

a=num%2000
b=num//2000

c=a%500
d=a//500

e=c%200
f=c//200

g=e%100
h=e//100

i=g%50
j=g//50

k=i%20
l=i//20

m=k%10
n=k//10

o=m%1
p=m//1


print("number of 2000 rupees notes requird:",b)
print("number of 500 rupees notes requird:",d)
print("number of 200 rupees notes requird:",f)
print("number of 100 rupees notes requird:",h)
print("number of 50 rupees notes requird:",j)
print("number of 20 rupees notes requird:",l)
print("number of 10 rupees notes requird:",n)
print("number of 1 rupees coin requied:",p)

total_amt=(2000*b+500*d+200*f+100*h+50*j+20*l+10*n+1*p)
print("total amount :",total_amt)
