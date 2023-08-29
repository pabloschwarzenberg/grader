#Aprobación de créditos
ingreso = input("Ingrese valor en pesos ")
anos = input("Ingrese edad ")
nh = input("Ingrese cantidad de hijo ")
ab = input("Ingrese cuantoss año pertenece al banco ")
ec = input("Estado civil ")
vi = input("Campo o ciudad ")

if ab > "10" and nh >= "2":
  print("APROBADO")
if ec == "C" and nh > "3" and "45" < anos < "55" :
  print("APROBADO")
if ingreso > "2500000" and ec == "S" and vi == "U":
  print("APROBADO")
if ingreso > "3500000" and ab > "5":
  print("APROBADO")
if vi == "R" and ec == "C" and nh < "2":
  print("APROBADO")
else:
  print("NO APROBADO")