#INGRESA LAS VARIABLES
a=int(input("Ingresa el valor de A: "))
b=int(input("Ingresa el valor de B: "))
c=int(input("Ingresa el valor de C: "))
d=int(input("Ingresa el valor de D: "))
e=int(input("Ingresa el valor de E: "))
f=int(input("Ingresa el valor de F: "))
#CUÁNTAS SOLUCIONES TIENE EL SISTEMA
if a/b == d/e and c!=f:
    print("No hay soluciones")
#CÁLCULO DEL VALOR DE Y
y =(d*c-a*f)/(d*b-a*e)
#CÁLCULO DEL VALOR DE X
x=(c-b*y)/a
print("X=", x)
print("Y=", y)