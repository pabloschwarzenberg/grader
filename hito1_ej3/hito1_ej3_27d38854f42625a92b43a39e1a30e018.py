#Aprobación de créditos

i=int(input("Ingreso"))
a=int(input("Año de nacimiento"))
n=int(input("Hijos"))
p=int(input("Años con el banco"))
e=input("Soltero o Casado")
l=input("Urbano o rural")

if p>10 and n>=2:
  print("APROBADO")
else:
  print("RECHAZADO")

if e=="C" and n>=45 and n<=55:
  print("APROBADO")
else:
  print("RECHAZADO")
if i>2500000 and e=="S" and l=="U":
  print("APROBADO")
else:
  print("RECHAZADO")
if i>3500000 and p>5:
  print("APROBADPO")
else:
  print("RECHAZADO")
if l=="R" and e=="C" and n<2:
  print("APROBADO")
else:
 print("RECHAZADO")

      