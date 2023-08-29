#Aprobación de créditos
Ingreso = eval(input("Ingrese su ingreso: "))
Añodenacimiento = input("Ingrese su año de nacimiento: ")
Númerodehijos = eval(input("Ingrese el numero de hijos que tiene: "))
ADPAB = eval(input("Ingrese sus años de pertenencia al banco: "))
Estadocivil =input("Ingrese su estado civil S/C: ")
CiOCa = input("Ingrese si reside en ciudad o campo U/R: ")
if (Estadocivil=="S" and CiOCa=="U" and Ingreso>2500000):
  print("APROBADO")
elif ADPAB>10 and Númerodehijos>=2:
  print("APROBADO")
elif Estadocivil=="C" and Númerodehijos>3 and 1976<Añodenacimiento<1966:
  print("APROBADO")
elif Ingreso>3500000 and ADPAB>5:
  print("APROBADO")
elif CiOCa=="R" and Estadocivil=="C" and Númerodehijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")