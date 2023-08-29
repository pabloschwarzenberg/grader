#Aprobación de créditos
ingreso=int(input("Ingreso:"))
nacimiento=int(input("Año de nacimiento:"))
edad=2021-nacimiento
hijos=int(input("Numero de hijos:"))
banco=int(input("Ingrece años en el banco:"))
casado=input("Ingrese S para soltero y C para casado:")
campo=input("Ingrese U para urbano y R para rural:")
S="S"
C="C"
U="U"
R="R"
aprobado=0

if banco >=10 and hijos >=2:
  aprobado+=1
if 55>=edad>=45 and hijos>=3:
  aprobado+=1
if ingreso>=2500000 and casado in S and campo in U:
  aprobado+=1
if ingreso>=3500000 and banco>=5:
  aprobado+=1
if campo in R and casado in C and hijos < 2:
 aprobado+=1

if aprobado>0:
  print("APROBADO")
else:
  print("RECHAZADO")
  