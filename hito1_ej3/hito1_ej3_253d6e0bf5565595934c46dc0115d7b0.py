#Aprobación de créditos
S=1
C=0
U=1
R=0
Ingreso=eval(input("Ingreso en pesos: "))
Ano=eval(input("Ingrese año de nacimiento: "))
hijos=eval(input("Numero de hijos: "))
Anosbanco=eval(input("Años de pertenencia al banco: "))
EC=eval(input("Es soltero o casado S/C: "))
coc=eval(input("Vive en Urbano o Rural U/R: "))
if Anosbanco > 10 and hijos >=2: 
  print("APROBADO")
elif EC == 0 and hijos > 3 and (2020-Ano) > 45 and (2020-Ano) >= 55:
  print("APROBADO")
elif Ingreso > 2500000 and EC == 1 and coc == 1:
  print("APROBADO")
elif Ingreso > 3500000 and Anosbanco > 5: 
  print("APROBADO")
elif coc == 0 and EC == 0 and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")   