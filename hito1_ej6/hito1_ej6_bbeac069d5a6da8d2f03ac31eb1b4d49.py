#Entrada

A = int(input("Ingrese el primer numero entero= "))
B = int(input("Ingrese el segundo numero entero= "))
C = int(input("Ingrese el tercer numero entero= "))

#Ordenacion
#Si A es mayor
if A > B and A > C :
    if B > C :
        print(str(C)+","+str(B)+","+str(A))
    else :
        print(str(B)+","+str(C)+","+str(A))

#Si B es mayor
elif B > A and B > C :
    if A > C :
        print(str(C)+","+str(A)+","+str(B))
    else :
        print(str(A)+","+str(C)+","+str(B))

#Si C es mayor
elif C > A and C > B :
    if B > A :
        print(str(A)+","+str(B)+","+str(C))
    else :
        print(str(B)+","+str(A)+","+str(C))
else :
    print("Todos son iguales")