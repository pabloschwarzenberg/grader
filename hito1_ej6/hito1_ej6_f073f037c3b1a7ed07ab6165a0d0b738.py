#Ordenar tres números
a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))
c = int(input("Ingrese numero 3: "))

a1 = min(a, b, c)
a3 = max(a, b, c)
a2 = (a+c+b) - a1 - a3

print("Numeros ordenados:" + str(a1) + "," + str(a2) + "," + str(a3))