#Ordenar tres números
n1 = int(input("Ingrese el primer número:"))
n2 = int(input("ingrese el segundo número:"))
n3 = int(input("ingrese el tercer número:"))
if n1 < n2 < n3:
    print("El orden de los números es:", n1,",", n2 ,",", n3)
elif n2 < n3 < n1:
    print("El orden de los números es:",n2,",",n3,",",n1 )
elif n3 < n1 < n2:
    print("El orden de los números es:",n3,",",n1,",",n2)
elif n1 == n3 < n2:
    print ("El orden de los números es:",n1,",",n3,",",n2)
elif n1 == n3 > n2:
    print("El orden de los números es:",n2,",",n1,",",n3)