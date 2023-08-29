#sistema de ecuaciones
a=int(input("Ingrese el numero a:  "))
b= int(input("Ingrese el numero b: "))
c= int(input("Ingrese el numero c: "))
d=int(input("Ingrese el numero d: "))
e=int(input("Ingrese el numero e: "))
f=int(input("Ingrese el numero f: "))

determinante= a*e - b*d
resultado_X=(c*e - b*f)/determinante
resultado_Y=(a*f - c*d)/determinante

print("x=",resultado_X)
print("y=",resultado_Y)