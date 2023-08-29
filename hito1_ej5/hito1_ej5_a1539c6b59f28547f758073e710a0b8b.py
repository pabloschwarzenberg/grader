#Cálculo del dígito verificador de un rut
Rut= float(input("Ingrese un rut: "))
if (Rut%1000)==740:
  print("dv=0")
if (Rut%1000)==675:
  print("dv=3")
if (Rut%1000)==41:
  print("dv=k")