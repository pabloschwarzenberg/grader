#Aprobación de créditos
ing= eval(input("ingreso: "))
nac= eval(input(" año nac: "))
hijos= eval(input("nro hijos: "))
pert= eval(input("años pret: "))
estado = input("(S:soltero,C:casado): ")
vive= input("(U:urbano,R:rural): ")

if pert > 10 and hijos >= 2:
  print("APROBADO")
elif estado == "C" and hijos > 3 and nac >= 1965 and nac <= 1975:
  print("APROBADO")
elif ing > 2500000 and estado == "S" and vive == "U":
  print("APROBADO")
elif ing > 3500000 and pert > 5:
  print("APROBADO")
elif vive == "R" and estado == "C" and hijos < 2:
  print("APROBADO")
else:
  print("REPROBADO")     
      