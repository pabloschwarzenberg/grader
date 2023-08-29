#Ordenar tres números
x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))

minimo = min(x, y, z)
maximo = max( x, y, z)
c = (x+y+z)-minimo-maximo

print(f"Los numeros ordenados de menor a mayor son: {minimo}, {c}, {maximo}")