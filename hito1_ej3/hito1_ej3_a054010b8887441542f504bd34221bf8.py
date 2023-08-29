#Aprobación de créditos
pesos=int(input("ingreso en peso:"))
nacimiento=int(input("año de nacimiento:"))
hijos=int(input("numero de hijos hijos:"))
anbanco=int(input("años de pertenencia al banco:"))
estado=str(input("S:soltero C:casado:"))
campo=str(input("U:urbano R:rural:"))
edad=(2021-nacimiento)
if anbanco >=10 and hijos >=2:  
    print("APROBADO")
elif str(estado)[:1]=="C" and hijos>=3 and edad>=45 and edad<55:
    print("APROBADO")
elif pesos>=250000 and str(campo)[:1]=="S":
  print("APROBADO")
elif pesos>=350000 and anbanco>5 :
   print("APROBADO")
elif str(estado)[:1]=="C" and str(campo)[:1]=="R" and hijos<=2:
  print("APROBADO")
else:
  print("RECHAZADO")
    
