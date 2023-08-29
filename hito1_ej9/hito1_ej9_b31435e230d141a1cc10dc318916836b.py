#Sistema de Ecuaciones
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))
d = int(input("Ingresa el cuarto numero: "))
e = int(input("Ingresa el quinto numero: "))
f = int(input("Ingresa el sexto numero: "))
det = a*e - b*d
if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        print("x=", x, "y=", y)