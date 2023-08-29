#Descomponer un número
n=int(input("Ingrese un número de cuatro digitos: "))

m=n//1000
r1=n%1000
c=r1//100
r2=r1%100
d=r2//10
u=r2%10

if m==0:
    print(str(c),"C+",str(d),"D+",str(u),"U")
elif m==0 and c==0:
    print(str(d),"D+",str(u),"U")
elif m==0 and c==0 and u==0:
    print(str(u),"U")
else:
    print(str(m),"M+",str(c),"C+",str(d),"D+",str(u),"U") 