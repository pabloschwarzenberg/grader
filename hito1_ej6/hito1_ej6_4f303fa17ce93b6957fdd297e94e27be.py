#Ordenar tres números
n1 = int(input("Ingrese Numero: "))
n2 = int(input("Ingrese Numero: "))
n3 = int(input("Ingrese Numero: "))
if n1>n2 and n1>n3:
    if n2>n3:
        print(str(n3)+","+str(n2)+","+str(n1))
    else:
        print(str(n2)+","+str(n3)+","+str(n1))
elif n2>n1 and n2>n3:
    if n1>n3:
        print(str(n3)+","+str(n1)+","+str(n2))
    else:
        print(str(n1)+","+str(n3)+","+str(n2))
else:
    if n1>n2:
        print(str(n2)+","+str(n1)+","+str(n3))
    else:
        print(str(n1)+","+str(n2)+","+str(n3)) 