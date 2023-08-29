a=int(input("ingresar sus ingresos(en pesos): "))
b=int(input("ingrese su año de nacimiento: "))
c=int(input("ingrese numero de hijos: "))
d=int(input("ingrese los años de pertenencia al banco: "))
e=input("estado civil: ")
f=input("donde vive: ")
if (b>=10) and (c>=2):
  print("APROBADO")
if (e=="C") and (c>3) and (1962<=b<=1972):
  print("APROBADO")
if (a>2500000) and (e=="S") and (f=="U"):
  print("APROBADO")
if (a>3500000) and (d>5):
  print("APROBADO")
if (f=="R") and (e=="C") and (c<2):
  print("APROBADO")
else:
  print("RECHAZADO")