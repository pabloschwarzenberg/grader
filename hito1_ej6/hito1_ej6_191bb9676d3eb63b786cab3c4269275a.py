#Ordenar tres números
n1=int(input("Escriba el primer numero: "))
n2=int(input("Escriba el segundo numero: "))
n3=int(input("Escriba el tercer numero: "))

if n1 < n2 < n3:
     print (("De menor a mayor el orden es el siguiente:"), n1,(","), n2,(","), n3)
     
elif n2 < n1 < n3:
    print (("De menor a mayor el orden es el siguiente:"), n2,(","), n1,(","), n3)
    
elif n3 < n1 < n2:
    print (("De menor a mayor el orden es el siguiente:"), n3,(","), n1,(","), n2)
    
elif n1 < n3 > n2:
    print (("De menor a mayor el orden es el siguiente:"), n1,(","), n2,(","), n3)
 
elif n1 and n2 > n3:
    print (("De menor a mayor el orden es el siguiente:"), n3,(","), n1,(","), n2)
    
elif n2 < n1 >n3:
    print (("De menor a mayor el orden es el siguiente:"), n2,(","), n3,(","), n1)

elif n2 and n3 > n1:
    print (("De menor a mayor el orden es el siguiente:"), n1,(","), n2,(","), n3)

elif n1 < n2 > n3:
    print (("De menor a mayor el orden es el siguiente:"), n1,(","), n3,(","), n2)

elif n1 and n3 > n2:
    print (("De menor a mayor el orden es el siguiente:"), n2,(","), n1,(","), n3)

else:
    print (("Los tres números son iguales:"), n1, ("="), n2, ("="), n3)
      