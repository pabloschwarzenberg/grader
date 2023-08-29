#Ordenar tres números

x = int(input("Introduzca el primer numero: "))
y = int(input("Introduzca el segundo numero: "))
z = int(input("Introduzca el tercer numero: "))
      
a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c
      
print("Los numeros ordenados son: {}, {}, {}" .format(a, b, c))