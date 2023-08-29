ingreso = eval(input("ingreso:"))
nacimiento = eval(input("año nac:"))
hijos = eval(input("nro hijos:"))
pertenece = eval(input("años pert:"))
estadocivil = input("(S:soltero,C:casado):")
vive = input("(U:urbano,R:rural)")

if pertenece > 10 and hijos >= 2:
  print("APROBADO")
elif estadocivil == "C" and hijos > 3 and nacimiento >= 1965 and nacimiento <= 1975:
  print("APROBADO")
elif ingreso > 2500000 and estadocivil == "S" and vive == "U":
  print("APROBADO")
elif ingreso > 3500000 and pertenece >5:
  print("APROBADO")
elif vive =="R" and estadocivil =="C" and hijos <2:
  print("APROBADO")
else:
  print("REPROBADO")
  