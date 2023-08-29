#Ordenar tres números


n1 = int(input("ecriba el primer  numero: "))
n2 = int(input("ecriba el segundo  numero: "))
n3 = int(input("ecriba el tercer  numero: "))


if n1 <= n2 <= n3:
    print ( "se ordena de la siguiente manera:",n1,",",n2,",",n3)
elif n1 <= n3 <= n2:
     print ("se ordena de la siguiente manera:",n1,",",n3,",",n2)
elif n2 <= n3 <= n1:
     print ("se ordena de la siguiente manera:",n2,",",n3,",",n1)
elif n2 <= n1 <= n3:
     print ("se ordena de la siguiente manera:",n2,",",n1,",",n3)
elif n3 <= n2 <= n1:
     print ("se ordena de la siguiente manera:",n3,",",n2,",",n1)
elif  n3 <= n1 <= n2:
     print ("se ordena de la siguiente manera:",n3,",",n1,",",n2)
else:
    print("numeros inalidos")
