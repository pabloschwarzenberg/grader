#Descomponer un número
x= int(input("ingrese un numero de hasta 4  digitos: "))

m=x//1000
print (m)

c1=x//100
c=c1%10
print(c)

d1=x//10
d=d1%10
print(c)

u=x%10
print(u)

print("{}M+{}C+{}D+{}U".format(m,c,d,u))