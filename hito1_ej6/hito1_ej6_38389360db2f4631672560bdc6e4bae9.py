#Ordenar tres números
#identificar o agregar nuestros numeros enteros

n = int (input ("Escriba el primer número:" ))
r = int(input("Escriba el segundo número: "))
z = int (input("Escriba el tercer número: "))

#calculo de minimo y maximo para el orden
a = min(n, r, z)
v = max(n, r, z)
b = (n + r + z) - a - v


print("El orden de los números enteros son los siguientes: {}, {}, {}". format (a, b, v))