#Aprobación de créditos
import datetime 
ingreso = int(input("cuales son sus ingresos?"))
anio = int(input("año de nacimiento?"))
Nhijos = int(input("numero de hijos?"))
anioBanco = int(input("años en este banco?"))
estadoC = input("estado civil?")
vive = input("ciudad o campo?")
fechaActual = datetime.datetime.now()
edad = fechaActual.year
anioNacimiento = edad - anio
aprobacion=0
if anioBanco>10 and Nhijos>=2:
    print("APROBADO")
    aprobacion = aprobacion+1
if estadoC=="C" and Nhijos>3 and anioNacimiento>=45 and anioNacimiento<=55 and aprobacion==0:
    print("APROBADO")
    aprobacion = aprobacion+1
if ingreso>=2500000 and estadoC=="S" and vive=="U" and aprobacion==0:
    print("APROBADO")
    aprobacion = aprobacion+1
if ingreso>=3500000 and anioBanco>5 and aprobacion==0:
    print("APROBADO")
    aprobacion = aprobacion+1
if vive=="R" and estadoC=="C" and Nhijos<2 and aprobacion==0:
    print("APROBADO")
if aprobacion==0:
    print("RECHAZADO")