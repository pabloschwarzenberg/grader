#Aprobación de créditos
i = int(input("ingresos: "))
a = int(input("año de nacimiento: "))
n = int(input("numero de hijos: "))
b = int(input("años de pertenencia al banco: "))
S = "Soltero"
C = "Casado"
e = input("Estado civil (S: soltero, C, casado): ")
U = "Urbano"
R = "Rural"
v = input("vive en campo o cuidad (U: urbano, R: rural):")
#condiciones
if b>10 and n>=2:
  print ("APROBADO")
elif e==C and n>3 and 1965>=a>=1975:
  print("APROBADO")
elif i>2500000 and e==S and v==U:
  print("APROBADO")
elif i>3500000 and b>5:
  print("APROBADO")
elif v==R and e==C and n<2:
  print("APROBADO")
else:
  print("NO APROBADO")