#Aprobación de créditos
ingreso=int(input("ingresa tu cantidad en pesos: "))
año=int(input("ingresa tu año de nacimiento: "))
hijos=int(input("ingresa la cantidad de hijos: "))
años_banco=int(input("ingresa tu cantidad de años en el banco: "))
estado_civil=input("ingresa tu estado civil: ")
lugar_vivir=input("ingresa donde vives: ")
b=2016-año

if años_banco>10 and hijos >=2:
    print("APROBADO")
    
elif estado_civil=="C" and hijos>3 and b>=45 and b<=55:
    print("APROBADO")

elif ingreso>2500000 and estado_civil=="S" and lugar_vivir=="U":
    print("APROBADO")

elif ingreso>3500000 and años_banco>5:
    print("APROBADO")

elif lugar_vivir=="R" and estado_civil=="C" and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")