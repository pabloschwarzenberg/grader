#Ordenar tres números
#Entrada.
Número1 = int(input("Ingrese el primer número: "))
Número2 = int(input("Ingrese el segundo número: "))
Número3 = int(input("Ingrese el tercer número: "))
#Procedimientos.
Números = [Número1,Número2,Número3]
Números.sort()
#Salida.
for x in Números:
  print(x)