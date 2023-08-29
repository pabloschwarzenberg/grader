#Aprobación de créditos
ing = eval(input("ingreso: "))
nac = eval(input("año nac: "))
hij = eval(input("nro. hijos: "))
per = eval(input("años de pertenencia al banco: "))
est = input("Estado Civil (S: soltero, C: casado): ")
viv = input("Lugar donde vive (U: urbano, R: rural): ")
if per > 10 and hij >= 2:
  print("APROBADO")
elif est == "C" and hij > 3 and nac >= 1965 and nac <= 1975:
  print("APROBADO")
elif ing > 2500000 and est == "S" and viv == "U":
  print("APROBADO")
elif ing > 3500000 and per > 5:
  print("APROBADO")
elif viv == "R" and est == "C" and hij < 2:
  print("APROBADO")
else:
  print("NO APROBADO")  