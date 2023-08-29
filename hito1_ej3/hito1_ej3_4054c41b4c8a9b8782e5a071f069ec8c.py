#Aprobación de créditos
S=1
C=0
U=1
R=0
Ingreso=eval(input("Ingreso en pesos: "))
Año=eval(input("Ingrese año de nacimiento: "))
hijos=eval(input("Ingrese numero de hijos: "))
Añosbanco=eval(input("Ingrese años de pertenencia al banco: "))
EC=eval(input("Es soltero o casado S/N: "))
coc=eval(input("Donde vive Urbano o Rural U/R: "))
if Añosbanco > 10 and hijos >=2: 
  print("APROBADO")
if EC == 0 and hijos > 3 and (2020-Año) > 45 and (2020-Año) >= 55:
  print("APROBADO")
if Ingreso > 2500000 and EC == 1 and coc == 1:
  print("APROBADO")
if Ingreso > 3500000 and Añosbanco > 5: 
  print("APROBADO")
if coc == 0 and EC == 0 and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO ") 