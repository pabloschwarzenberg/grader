#Aprobación de créditos
ingreso=input("Ingrese su sueldo mensual: ")
año_nacimiento=input("Ingrese su año de nacimiento: ")
numero_hijos=input("Ingrese el numero de hijos vivos: ")
años_banco=input("Ingrese los años de pertenencia al banco que posee: ")
estado_civil=input("Ingrese C si está casado o S si esta soltero")
residencia=input("Ingrese R si vive en el campo y U si vive en la ciudad")
edad= int(2017-(float(año_nacimiento)))
Credito_rechazado=True

if años_banco>="10" and numero_hijos>="2":
 Credito_rechazado=False
 print("Credito APROBADO")

if estado_civil=="C" and numero_hijos>"3" and edad==[45,56]:
 Credito_rechazado=False
 print("Credito APROBADO")
 
if ingreso>"2500000" and estado_civil=="S" and residencia=="U":
 Credito_rechazado=False
 print("Credito APROBADO")

if ingreso>"3500000" and años_banco>"5":
 Credito_rechazado=False
 print("Credito APROBADO")

if residencia=="R" and estado_civil=="C" and numero_hijos<"2":
 Credito_rechazado=False
 print("Credito APROBADO")

else:
 Credito_rechazado=True
 print("Credito RECHAZADO")