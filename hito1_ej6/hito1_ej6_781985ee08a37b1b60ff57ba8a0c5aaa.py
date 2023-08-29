#Ordenar tres números
a=int(input("Escriba el primer número: "))
b=int(input("Escriba el segundo número: "))
c=int(input("Escriba el tercer número: "))

x=min(a, b, c) #relación mínima de orden para los números ingresados.
z=max(a, b, c) #relación máxima de orden para los números ingresados.
y=(a+b+c)-x-z

print("Así serían los números ordenados: {}, {}, {}".format(x, y, z))