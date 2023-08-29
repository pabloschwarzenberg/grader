#Ordenar tres números

#ENTRADA 
n1= int(input("ingrese el primer número:"))
n2= int(input("ingrese el segundo número:"))
n3= int(input("ingrese el tercero número:"))

#COMPROBACION

if n1 <= n2 and n1 <= n3:
    x = n1
    if n2 <= n3:
        y = n2
        z = n3
    else: 
        y = n3
        z = n2

elif n2 <= n1 and n2 <= n3:
    x = n2
    if n1<= n3:
        y = n1
        z = n3
    else:
        y = n3
        z = n1
    
else: 
    x = n3
    if n1<= n2:
        y = n1
        z = n2
    else:
        y = n2
        z = n1

#SALIDA
        
print(str(x) + "," + str(y) + "," + str(z))
print("Fin.")     