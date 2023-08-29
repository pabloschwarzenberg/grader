plata=eval(input("ingresos en pesos"))
año_nacimiento=eval(input("ingrese año de nacimiento"))
hijos=eval(input("ingrese numero de hijos"))
pertenencia=eval(input("años de pertenencia en el banco"))
estado_civil=input("ingrese su estado civil")
residencia=input("vives en campo o ciudad")

if(pertenencia>10) and (hijos>=2):
    print("APROBADO")
elif(estado_civil=="C")and(hijos>=3)and(1966<=año_nacimiento>=1976):
    print("APROBADO")
elif(plata>2500000)and(estado_civil=="S")and(residencia=="U"):
    print("APROBADO")
elif(plata>3500000)and(pertenencia>5):
    print("APROBADO")
elif(residencia=="R")and(estado_civil=="C")and(hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")