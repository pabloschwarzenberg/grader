def soluciones(n1,n2,n3,n4,n5,n6):
 det = n1*n5 - n2*n4
 if det !=0:
 
    x = (n3*n5 - n2*n6)/det
    y = (n1*n6 - n3*n4)/det

    print("x=", x, "y=", y)
 else:
     return None, None
n1 = int(input("Ingrese num 1:"))
n2 = int(input("Ingrese num 2:"))
n3 = int(input("Ingrese num 3:"))
n4 = int(input("Ingrese num 4:"))
n5 = int(input("Ingrese num 5:"))
n6 = int(input("Ingrese num 6:"))

print(soluciones(n1,n2,n3,n4,n5,n6))