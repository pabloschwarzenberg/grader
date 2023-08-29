#a=ingreso en pesos
a=int(input())
#b=año de nacimiento
b=int(input())
#c=numero de hijos
c=int(input())
#d=años de pertenencia al banco
d=int(input())
#e=estado civil
e=input()
#f=si vive en el campo o ciudad
f=input()

if(d>10):
  if(c>=2):
    print("APROBADO")
else:
    print("RECHAZADO")
    
if(e=="C"):
  if(c>3):
    if(1962<b<1972):
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


    






