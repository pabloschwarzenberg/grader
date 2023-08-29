#Ordenar tres números
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

#Comparación de números

if n1 >= n2 >= n3 :
    print(str(n3) + "," + str(n2) + "," + str(n1))
elif n3 >= n2 >= n1 :
    print(str(n1)  + "," + str(n2) + "," + str(n3))
elif n2 >= n1 >= n3 :
    print(str(n3) + "," + str(n1) + "," + str(n2))
elif n3 >= n1 >= n2 :
    print(str(n2) + "," + str(n1) + "," + str(n3))
elif n2 >= n3 >= n1 :
    print(str(n1) + "," + str(n3) + "," + str(n2))
elif n1 >= n3 >= n2 :
    print(str(n2) + "," + str(n3) + "," + str(n1))
    
