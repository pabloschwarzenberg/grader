#Aprobación de créditos
i=int(input("Ingreso:"))
a=int(input("Año de nacimiento:"))
n=int(input("Numero de hijos:"))
b=int(input("Años de pertenencia al banco:"))
c=input("Estado civil:")
v=input("Vive en:")

if b>10 and n>=2:
  print("APROBADO")
elif c=="C" and n>=3 and 45<=int(2017-a)<=55 :
  print("APROBAD0")
elif i>2500000 and c=="S"and v=="U":
  print("APROBADO")
elif i>3500000 and b>5:
  print("APROBADO")
elif v=="R" and c=="C" and n<2:
  print("APROBADO")
else:
  print("RECHAZADO")
