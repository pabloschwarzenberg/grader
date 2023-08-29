#Aprobación de créditos
from datetime import datetime
ingreso = int(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su número de hijos: "))
pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
residencia = input("Ingrese si vive en campo o ciudad (U: urbano, R: rural): ")

edad = datetime.now().year - nacimiento

if (pertenencia > 10 and hijos >= 2) or (estado_civil == "C" and hijos > 3 and 45 <= edad <= 55) or (ingreso > 2500000 and estado_civil == "S" and residencia == "U") or (ingreso > 3500000 and pertenencia > 5) or (residencia == "R" and estado_civil == "C" and hijos < 2):
    print("Resultado: APROBADO")
else:
    print("Resultado: RECHAZADO")    