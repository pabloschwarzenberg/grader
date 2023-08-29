#Ordenar tres números

menor=0
mayor=0
mediano=0
#Ordenar tres números

a=int(input("Ingrese el primer número entero :"))
b=int(input("Ingrese el segundo número entero :"))
c=int(input("Ingrese el tercer número entero :"))


if a>b and a>c:
    mayor=a

elif b>a and b>c:
    mayor=b

elif c>a and c>b:
    mayor=c

if a<b and a<c:
    menor=a

elif b<a and b<c:
    menor=b

elif c<a and c<b:
    menor=c
if a<b and a>c:
    mediano=a
elif b<a and b>c:
    mediano=b
else:
    mediano=c

print(" el numero menor es :" , menor )

print(" el numero del medio es :" , mediano )

print(" el numero mayor es :" , mayor )

print(menor,mediano,mayor,sep=",")