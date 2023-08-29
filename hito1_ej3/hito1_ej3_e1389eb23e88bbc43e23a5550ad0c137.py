#Aprobación de créditos
print("Ingrese datos solicitados")
i=int(input("Ingreso en $="))
n=int(input("año de nacimiento:"))
h=int(input("numero de hijos:"))
pb=int(input("años de pertenecencia al banco:"))
ec=input("estado civil(C=casado, S=Soltero):")
v=input("ingrese U si vive en ciudad o R si vive en campo:")

if pb>10 and (h>=2):
  print("APROBADO")
elif ec == "C" and (h>3) and (n>=1961) and (n<=1971):
  print("APROBADO")
elif i>2500000 and ec == "S" and v == "U":
  print("APROBADO")
elif i>3500000 and pb>5:
  print("APROBADO")
elif v == "R" and ec == "C" and (h<2):
  print("APROBADO")
  
else:
    print("RECHAZADO") 