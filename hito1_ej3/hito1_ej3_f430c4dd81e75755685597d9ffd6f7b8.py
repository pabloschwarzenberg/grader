#Aprobación de créditos
a=int(input("¿Cuál es su ingreso mensual?"))
b=int(input("¿Cuál es su año de nacimiento?"))
c=int(input("¿Cuántos hijos tiene?"))
d=int(input("¿Cuántos años ha sido cliente del banco?"))
e=input("¿Cuál es su estado civil? Responda S si está soltero, C si está casado.")
f=input("¿Vive en campo (R) o ciudad (U)? Responda con las letras según corresponda.")
if d>10 and c>=2:
  print("APROBADO")
elif e=="C" and c>3:
  if 45<(2016-b) and (2016-b)<55:
    print("APROBADO")
  else: 
    print("RECHAZADO")
elif a>2500000 and e=="S":
   if f=="U":
      print("APROBADO")
   else:
      print("RECHAZADO")
elif a>3500000 and d>5:
  print("APROBADO")
elif f=="R" and e=="C":
   if c<2:
      print("APROBADO")
   else:
      print("RECHAZADO")
else:
  print("RECHAZADO")
   