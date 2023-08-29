#Aprobación de créditos

#VARS
ingreso=int(input("Ingreso (en pesos): "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
vanguardia=int(input("Años de pertenencia al banco: "))
estado_civil=input("Estado civil (\"S\": soltero, \"C\", casado): ")
domicilio=input("Si vive en campo o cuidad (\"U\": urbano, \"R\": rural): ")
edad=abs(nacimiento-2023)
passed=0

#DEV OVERRIDE --ignore
#edad=50
#print(edad)

while(passed!=1):
    if(vanguardia>=10 and hijos>=2):
        passed=1
    if(estado_civil=="S" and hijos>3 and 45<=edad<=55):
        passed=1
    if(ingreso>2500000 and estado_civil=="S" and domicilio=="U"):
        passed=1
    if(ingreso>3500000 and vanguardia>5):
        passed=1
    if(domicilio=="R" and estado_civil=="C" and hijos<2):
        passed=1

if(passed==1):
    print("APROBADO")
else:
    print("RECHAZADO")
