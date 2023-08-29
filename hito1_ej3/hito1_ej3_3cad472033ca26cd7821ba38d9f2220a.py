#Aprobación de créditos
Ingreso=float(input("Digite su ingreso mensual: "))
Nacimiento=int(input("Digite el año de su nacimiento: "))
Hijos=int(input("Ingrese la cantidad de hijos que tiene: "))
Banco=float(input("Digite la cantidad de años desde que ha sido cliente del banco: "))
Estado=input("¿Estado civil? Use S si es Soltero y C si es casado: ")
Vivienda=input("¿Vive usted en campo o ciudad? Use U si vive en ciudad y R si vive en campo: ")
#Calculo
años=Nacimiento-2022
EU=Estado.upper()

if Banco>=10 and Hijos>= 2:print("APROBADO")

elif Estado.upper()=="C" and Hijos>=3 and años>=45 or años==55:print("APROBADO")

elif Ingreso>=2500000 and Estado=="S" and vivienda=="U":print("APROBADO")

elif Ingreso>=3500000 and Banco>=5:print("APROBADO")

elif Vivienda=="R" and Estado=="C" and Hijos<=2:print("APROBADO")

else:print("RECHAZADO")