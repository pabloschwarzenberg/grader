#Aprobación de créditos
ingreso=int(input("Ingreso (en pesos): "))
anno=float(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
anpert=float(input("Años de pertenencia al banco: "))
stat=input("Estado civil (S / C): ")
local=input("Campo o ciudad? (U / R): ")

if anpert>10 and hijos>=2:
  print("APROBADO")
elif stat=="C" and hijos>3 and 1963<=anno and anno<=1973:
  print("APROBADO")
elif ingreso>2500000 and stat=="S" and local=="U":
  print("APROBADO")
elif ingreso>3500000 and anpert>5:
  print("APROBADO")
elif local=="R" and stat=="C" and hijos<=2:
  print("APROBADO")
else:
  print("REPROBADO")