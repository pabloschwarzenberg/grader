#Ordenar tres números
print("Hola!")
print("Ingresa 3 numeros para ordenar de menor a mayor:")
d=int(input("Numero 1: "))
e=int(input("Numero 2: "))
f=int(input("Numero 3: "))

if d>=e>=f:
	print("El orden de menor a mayor es:")
	print(f, e, d)
elif d>=f>=e:
	print("El orden de menor a mayor es:")
	print(e, f, d)
elif e>=d>=f:
	print("El orden de mayor a menor es:")
	print(f, d, e)
elif e>=f>=d:
	print("El orden de mayor a menor es:")
	print(d, f, e)
elif f>=e>=d:
	print("El orden de menor a mayor es:")
	print(d, e, f)
elif f>=d>=e:
	print("El orden de menor a mayor es:")
	print(e, d, f)
else:
	print("Todos los numeros son iguales")

print("_________________________________")