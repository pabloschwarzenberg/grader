#Aprobación de créditos
ingreso =int(input("ingrese su ingreso en pesos: "))
anodenac = int(input("ingrese año de nacimiento: "))
ndehijos = int(input("ingrese numero de hijos: "))
anosdeper = int(input("ingrese años de permanencia al banco:"))
print("C)Casado S)Soltero")
estadocivil =input("ingrese si es casado o soltero: ")
print("U)urbana R)rural")
vive = input("ingrese si vive en zona urbana o rural: ")
if (anosdeper>=10 and ndehijos>=2):
  print("APROBADO")
elif (estadocivil=="C" and ndehijos>3 and (anodenac<1973 or anodenac>1963)):
  print("APROBADO")
elif (ingreso>2500000 and estadocivil=="S" and vive=="U"):
  print("APROBADO")
elif (ingreso>3500000 and anosdeper>5):
  print("APROBADO")
elif (vive=="R" and estadocivil=="C" and ndehijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")
