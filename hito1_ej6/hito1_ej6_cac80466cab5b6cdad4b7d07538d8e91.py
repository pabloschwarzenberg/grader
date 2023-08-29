#Ordenar tres números
n1 = int(input("Ingrese el primer numero 1: "))
n2 = int(input("Ingrese el segundo numero 2: "))
n3 = int(input("Ingrese el tercer numero 3: "))
primero = min(n1, n2, n3)
tercero = max(n1, n2, n3)
segundo = (n3+n2+n1)-(primero+tercero)
print("El orden de menos a mayor es: ")
print(primero,",", segundo,",", tercero)      