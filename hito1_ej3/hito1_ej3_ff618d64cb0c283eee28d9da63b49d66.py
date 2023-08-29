#Aprobación de créditos
a=int(input())
#a=ingreso en pesos
b=int(input())
#b=año de nacimiento
c=int(input())
#c=numero de hijos
d=int(input())
#d=años de pertenencia
e=input()
#e=estado civil
f=input()
#lugar de residencia

if(d>10):
  if(c>1):
    print("APROBADO")
  else:
    print("RECHAZADO")

if(e=="C"):
  if(c>3):
    if(1962>b>1972):
      print("APROBADO")
  else:
    print("RECHAZADO")

if(a>2500000):
  if(e=="S"):
    if(f=="U"):
      print("APROBADO")
  else:
    print("RECHAZADO")
    
if(a>3500000):
  if(d>5):
    print("APROBADO")
  else:
    print("RECHAZADO")
    
if(f=="R"):
  if(e=="C"):
    if(c<2):
      print("APROBADO")
  else:
    print("RECHAZADO")