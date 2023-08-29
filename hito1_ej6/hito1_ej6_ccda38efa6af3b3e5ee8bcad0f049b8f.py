#ordenar tres números
#Ejercicio Katalina Diaz
a=int(input("ingrese el pimer valor a ordenar"))
b=int(input("ingrese el segundo valor a ordenar"))
c=int(input("ingrese el tercer valor a ordenar"))
aux=0
if (a>b):
    aux=a
    a=b
    b=aux
if (a>c):
    aux=a
    a=c
    c=aux
if (b>c):
    aux=b
    b=c
    c=aux
print("el orden de los numeros de menor a mayor es ",a,",", b,",",c)