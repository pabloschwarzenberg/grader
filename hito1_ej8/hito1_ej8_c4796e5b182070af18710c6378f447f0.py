#Descomponer un número
n=int(input("Ingrese un número que tenga máximo cuatro dígitos:"))
m=n//1000
c=(n//100)%10
d=(n//10)%10
u=n%10
print(m,"M +",c,"C +",d,"D +",u,"U")