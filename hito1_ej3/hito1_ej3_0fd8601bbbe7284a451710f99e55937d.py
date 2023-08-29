ingreso=int(input("Ingrese su ingreso (en pesos):"))
año_nacimiento=int(input("Ingres su año de nacimiento:"))
hijos=int(input("Ingrese numero de hijos:"))
años_banco=int(input("Ingrese sus años de pertenencia al banco:"))
civil=input("Ingrese su estado civil(S: soltero, C, casado):")
zona=input("Si vive en campo o cuidad ("U": urbano, "R": rural):")

año=2022
edad=año - año_nacimiento

if(años_banco>10 and hijos>=2):
    print("APROBADO")
elif(civil=="C" and hijos>3 and edad>45 and edad<55):
    print("APROBADO")
elif(ingreso>2500000 and civil=="S" and zona=="U"):
    print("APROBADO")
elif(ingreso>3500000 and años_banco>5):
    print("APROBADO")
elif(zona=="R" and civil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")