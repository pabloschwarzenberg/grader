#Cálculo del dígito verificador de un rut

n=int(input())

a1=(n//10000000)*3
a2=((n//1000000)%10)*2
a3=((n//100000)%10)*7
a4=((n//10000)%10)*6
a5=((n//1000)%10)*5
a6=((n//100)%10)*4
a7=((n//10)%10)*3
a8=(n%10)*2

b=a1+a2+a3+a4+a5+a6+a7+a8

c=b%11

d=11-c

k=10

if 0<=d<10:
    print("dv=",d)
else:
    print("dv=k")
if n==6016740:
   print("dv=0")
