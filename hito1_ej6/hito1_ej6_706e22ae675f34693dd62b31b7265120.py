#Ordenar tres números
#Entrada

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un 2do numero: "))
c = int(input("Ingrese un 3er numero: "))


#Solucion

if a >= b:
    if b >= c:
        print("El orden de menor a mayor es: "+ str(c) + "," + str(b) + "," + str(a))
    elif b <= c and c <= a:
        print("El orden de menor a mayor es: "+ str(b) + "," + str(c) + "," + str(a))
    elif b <= c and c >= a:
        print("El orden de menor a mayor es: "+ str(b) + "," + str(a) + "," + str(c))
if a <= b:
    if b <= c:
        print("El orden de menor a mayor es: "+ str(a) + "," + str(b) + "," + str(c))
    elif b >= c and a <= c:
        print("El orden de menor a mayor es: "+ str(a) + "," + str(c) + "," + str(b))
if a >= c and b >= c and b >= a:
    print("El orden de menor a mayor es: "+ str(c) + "," + str(a) + "," + str(b))
