#Ordenar tres números

#Ingreso de datos
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

# Operacion
if n1 <= n2 <= n3:
    no = n1, n2, n3
elif n1 <= n3 <= n2:
    no = n1, n3, n2
elif n2 <= n1 <= n3:
    no = n2, n1, n3
elif n2 <= n3 <= n1:
    no = n2, n3, n1
elif n3 <= n1 <= n2:
    no = n3, n1, n2
else: 
    no = n3, n2, n1

#Resupuesta
print("los numeros ordenados de menor a mayor son" ,no)
