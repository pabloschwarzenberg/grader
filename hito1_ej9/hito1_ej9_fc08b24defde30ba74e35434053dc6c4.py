a=int(input("Ingrese el numero a "))
b= int(input("Ingrese el numero b: "))
c= int(input("Ingrese el numero c: "))
d=int(input("Ingrese el numero d: "))
e=int(input("Ingrese el numero e: "))
f=int(input("Ingrese el numero f: "))

determinante= a*e - b*d

resultado_X=float(c*e - b*f)//determinante
resultado_Y=float(a*f- c*d)//determinante

print("X=",resultado_X)
print("Y=",resultado_Y)