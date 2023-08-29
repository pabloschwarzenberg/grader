#Aprobación de créditos
from datetime import datetime
Ingreso=int(input("Digite la cantidad total de ingresos:\n"))
n=input("Ingrese año de nacimiento:\n")
fecha = datetime.strptime(n, '%Y') # Tipo: datetime.datetime
hoy = datetime.now()      # Tipo: datetime.datetime
diferencia = hoy - fecha  # Tipo resultante: datetime.timedelta
añosTotal=round(diferencia.days/365)
numeroHijos=int(input("Ingrese la cantidad de Hijos que tiene:\n"))
pertenenciaBanco=int(input("Ingrese los años de pertenencia al banco\n"))
estadoCivil=input("Ingrese su estado civil, S: soltero o C: casado\n")
estadoDeVivienda=input("Ingrese si vive en campo o ciudad, U: urbano o R: rural\n")

if pertenenciaBanco>10 and numeroHijos>=2:
    print("APROBADO")
elif estadoCivil=='C' and numeroHijos>3 and añosTotal>=45 and añosTotal<=55:
    print("APROBADO")
elif Ingreso>2500000 and estadoCivil=='S' and estadoDeVivienda=='U':
    print("APROBADO")
elif Ingreso>3500000 and pertenenciaBanco>5:
    print("APROBADO")
elif estadoDeVivienda=='R' and estadoCivil=='C' and numeroHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")