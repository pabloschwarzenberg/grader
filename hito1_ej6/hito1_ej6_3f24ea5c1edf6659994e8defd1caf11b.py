#Ordenar tres números
#Entrada
print("Escriba tres valores los cuales serán mostrados en pantalla ordenados de menor a mayor")
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

#Valores
x = min(a, b, c)
z = max(a, b, c )
y = (a + b + c ) - x - z

#Respuesta  
print("El orden de los números de menor a mayor es: {},{},{}".format(x, y, z)) 