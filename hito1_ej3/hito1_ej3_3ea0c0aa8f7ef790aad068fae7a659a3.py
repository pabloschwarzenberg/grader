#Aprobación de créditos
ingreso=int(input("Ingreso:$"))
nacimiento=input("Año de nacimiento: ")
hijos=int(input("Número de hijos: "))
antiguedad=int(input("Años de pertenencia al banco" ))
estado_civil= input("Estado civil (S/soltero o C/casado):").lower
ubicacion= input("Si vive en campo o cuidad (U/urbano, R/rural)").lower
c=""
s=""
u=""
r=""
if (antiguedad>=10 and hijos>=1):
    print("APROBADO")
if(estado_civil==c and hijos>=1 and 1967<nacimiento<1977):
    print("APROBADO")
if (ingreso>2500000<ingreso<3500000 and estado_civil==s and ubicacion==u ):
    print("APROBADO")
if (ingreso>3500000 and antiguedad>=5):
    print("APROBADO")
if(ubicacion==r and estado_civil==c and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")