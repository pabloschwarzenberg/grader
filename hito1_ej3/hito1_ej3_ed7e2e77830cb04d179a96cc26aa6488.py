#Aprobación de créditos
ingreso=int(input("Ingreso: "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("N° de hijos: "))
banco=int(input("Años de pertenencia al banco: "))
civil=str(input("Estado civil (S: SOLTERO, C: CASADO): "))
vive=str(input("¿Donde vive?(U: URBANO, R: RURAL): "))
edad=2020-nacimiento
if banco>10 and hijos>=2:
  print("APROBADO")
elif civil=="C" and hijos>3 and 45<=edad<=55:
  print("APROBADO")
elif ingreso>2500000 and civil=="S" and vive=="U":
  print("APROBADO")
elif ingreso>3500000 and banco>5:
  print("APROBADO")
elif vive=="R" and civil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")