#Aprobación de créditos
#Entradas
naci = int(input("El año de nacimiento de quien solicita es: "))
ingre = int(input("La cantidad de ingresos de quien solicita es: "))
num_hij = int(input("La cantidad de hijos del solicitante: "))
perten = int(input("La cantidad de años perteneciendo al banco es: "))
est_civil = str(input("Ingresar S si es soltero o C si es casado: "))
vivien = str(input("Ingresar según zona, R si es rural o U si es urbano: "))


#Ecuación
edad = int(2021-naci)

if (perten > 10 and num_hij >= 2):
    print ("APROBADO")
elif (est_civil == "C" and num_hij > 3 and ( 45 <= edad <= 55)):
    print("APROBADO")
elif ( ingre > 2500000 and est_civil == "S" and vivien == "U"):
    print("APROBADO")
elif (ingre > 3500000 and perten > 5):
    print("APROBADO")
elif (est_civil == "C" and vivien == "R" and num_hij < 2):
    print("APROBADO")
else:
    print("RECHAZADO")