ingreso=eval(input("ingrese el dinero"))
año=eval(input("ingrese el año"))
hijos=eval(input("ingrese los hijos"))
añobanco=eval(input("ingrese los años al banco"))
civil=input("ingrese estado civil")
vivienda=input("ingrese donde vive")

S=60
U=70
R=80
C=90

if(10<año) and (2<=hijos):
  print("APROBADO")
if(civil) and (3<hijos) and ( 45<=año<=55):
  print("APROBADO")
if(2500000<ingreso) and (civil=="S") and (vivienda=="U"):
  print("APROBADO")
if(3500000<ingreso) and (añobanco<5):
  print("APROBADO")
if(vivienda=="R") and (civil=="C") and (hijos<2):
  print("APROBADO")