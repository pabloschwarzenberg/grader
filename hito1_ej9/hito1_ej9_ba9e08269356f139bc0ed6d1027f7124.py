#Sistema de Ecuaciones
n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese un numero: "))
n3 = int(input("ingrese un numero: "))
n4 = int(input("ingrese un numero: "))
n5 = int(input("ingrese un numero: "))
n6 = int(input("ingrese un numero: "))

fy = ((n6*n1)-(n4*n3))/((n1*n5)-(n4*n2))

fx = (n3-n2*fy)/n1

fy = round(fy,1)
fx = round(fx,1)

print("x=",fx, "y=",fy)
   