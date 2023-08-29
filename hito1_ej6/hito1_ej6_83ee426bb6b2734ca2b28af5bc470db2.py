#Ordenar tres números#
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el segundo número: "))

#Desarrollo#
d=min(a,b,c)
e=max(a,b,c)
f=(a+b+c)-d-e
print('El orden de los números es: {}, {}, {}'.format(d,f,e))