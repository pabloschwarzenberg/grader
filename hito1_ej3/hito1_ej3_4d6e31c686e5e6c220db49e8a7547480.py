ingreso=int(input())    
nacimiento=int(input()) 
hijos=int(input()) 
pertenencia=int(input()) 
civil=str(input())
vive =str(input())

if pertenencia>10:
  if hijos>=2:
     print("APROBADO")
else:
  print("RECHAZADO")
  
if civil==("C"):
  if hijos>3:
    if 45<2018-nacimiento<55:
      print("APROBADO")
else:
  print("RECHAZADO")
  
if ingreso>2500000:
  if civil==("S"):
    if vive==("U"):
      print("APROBADO")
else:
  print("RECHAZADO")
if ingreso>3500000:
  if pertenencia>5:
    print("APROBADO")
else:
  print("RECHAZADO")
if vive==("R"):
  if civil==("C"):
    if hijos<2:
      print("APROBADO")
else:
  print("RECHAZADO")
    