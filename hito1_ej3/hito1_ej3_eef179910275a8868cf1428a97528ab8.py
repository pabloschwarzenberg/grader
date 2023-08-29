#Aprobación de créditos
from datetime import datetime
now =datetime.now()
ing=eval(input("Ingreso"))
edad=now.year-eval(input("Año de nacimiento"))
hijos=eval(input("Cuantos hijos tiene"))
pert=eval(input("años de pertenencia"))
if input("estado civil")=="S":
    est=1
else:
    est=0
if input("lugar")=="U":
    lugar=1
else:
    lugar=0
if pert>10 and hijos>=2:
    print("APROBADO")
elif est==1 and hijos>3 and 45<edad<55:
    print("APROBADO")
elif ing>2500000 and est==1 and pert==1:
    print("APROBADO")
elif ing>3500000 and pert>5:
    print("APROBADO")
elif lugar==0 and est==0 and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")