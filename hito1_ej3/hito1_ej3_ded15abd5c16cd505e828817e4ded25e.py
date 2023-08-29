#Aprobación de créditos
ing=int(input("Ingrese su sueldo en pesos: "))
nac=int(input("Ingrese su año de nacimiento: "))
hij=int(input("Ingrese numero de hijos: "))
ban=int(input("Ingrese años de pertenencia al banco: "))
civ=input("Ingrese S si esta soltero, si esta casado, ingrese C")
viv=input("Ingrese U si vive en zona urbana, C si vive en zona rural")

if (ban>10 and hij>=2) or (civ=="C" and hij>3 and 45<=(2018-nac)<=55) or (ing>2500000 and civ=="S" and viv=="U") or (ing>3500000 and ban>5) or (viv=="R" and civ=="C" and hij<2):
  print("APROBADO")
else:
  print("RECHAZADO")