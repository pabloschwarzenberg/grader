#Descomponer un número
n=int(input("ingrese un numero de no mas de cuatro digitos: "))
a=n//10**3
b=(n//10**2)-10*a
c=((n//10)-(100*a+10*b))
d=((n%10**3)%10**2)%10
print(a,"M" ,"+",b,"C" ,"+", c,"D","+",d, "U")
