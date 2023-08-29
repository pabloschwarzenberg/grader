#Ordenar tres números
n1 = int(input("ingrese el primer numero :"))
n2 = int(input("ingrese el segundo numero : " ))
n3 = int(input("ingrese el tercer numero : " ))

if n1 > n2 and n1 > n3 and n2 > n3:
    print("el numero de menor a mayor es : " ,n3, "," ,n2, "," ,n1)
elif n1 >n2 and n1 > n3 and n2 < n3:
    print("el numero de menor a mayor es : " ,n2, "," ,n3, "," ,n1)
elif n2 > n1 and n2 > n3 and n1 > n3:
    print("el numero de menor a mayor es : " ,n3, "," ,n1, "," ,n2)
elif n2 > n1 and n2 > n3 and n1 < n3:
    print("el numero de menor a mayor es : " ,n1, "," ,n3, "," ,n2)
elif n3 > n1 and n3 > n2 and n1 < n2:
    print("el numero de menor a mayor es : " ,n1, "," ,n2, "," ,n3)
elif n3 > n1 and n3 > n2 and n1 > n2:
    print("el numero de menor a mayor es : " ,n2, "," ,n1, "," ,n3)
#sin dan mismimos numeros
elif n1 == n2 > n3:
    print("el numero de menor a mayor es : " ,n3, "," ,n2, "," ,n1)
elif n1== n2 < n3:
    print("el numero de menor a mayor es : " ,n2, "," ,n1, "," ,n3)
elif n1 == n3 > n2:
    print("el numero de menor a mayor es : " ,n2, "," ,n1, "," ,n3)
elif n1 == n3 < n2:
    print("el numero de menor a mayor es : " ,n1, "," ,n3, "," ,n2)
else:
    print("son todos el mismo numero")
