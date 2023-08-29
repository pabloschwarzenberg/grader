#Aprobación de créditos

# Online Python - IDE, Editor, Compiler, Interpreter
import datetime

date = datetime.date.today()
year = date.strftime("%Y")

datos = []
titulos =["Ingreso (en pesos)","Año de nacimiento","Número de hijos","Años de pertenencia al banco","Estado civil (S: soltero, C: casado)","Si vive en campo o cuidad (U: urbano, R: rural)"]

for i in range(6):
   datos.append(input(titulos[i]))
    
print(datos)

if((int(datos[3])>10) or ((datos[4].lower() == "c") and (int(datos[2])>3) and (((int(year)-int(datos[1]))>=45) or ((int(year)-int(datos[1]))<=55))) or ((int(datos[0])>2500000) and (datos[4].lower() == "s") and (datos[5].lower() == "u")) or ((int(datos[0])>3500000) and (int(datos[3]>10))) or ((datos[5].lower() == "r") and (datos[4].lower() == "c") and (int(datos[2])>2))):
    print("APROBADO")
else:
    print("RECHAZADO")