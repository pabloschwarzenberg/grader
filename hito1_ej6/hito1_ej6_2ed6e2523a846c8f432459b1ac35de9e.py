#Ordenar tres números
n1 = int(input("Ingrese Numero 1 :"))
n2 = int(input("Ingrese Numero 2 :"))
n3 = int(input("Ingrese Numero 3 :"))
if (n1 <= n2) and (n1 <= n3) and (n2 <= n3):
    print (n1,",",n2,",",n3)
elif (n1 <= n2) and (n1 <= n3) and (n2 >= n3):
    print (n1,",",n3,",",n2)
elif (n1 >= n2) and (n1 <= n3) and (n2 <= n3):
    print (n2,",",n1,",",n3)
elif (n1 >= n2) and (n1 <= n3) and (n2 >= n3):
    print (n3,",",n1,",",n2)
elif (n1 >= n2) and (n1 >= n3) and (n2 >= n3):
    print (n3,",",n2,",",n1)
elif (n1 >= n2) and (n1 >= n3) and (n2 <= n3):
    print (n2,",",n3,",",n1)
