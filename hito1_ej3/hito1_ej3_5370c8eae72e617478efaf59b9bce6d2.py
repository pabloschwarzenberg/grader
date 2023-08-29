#Aprobación de créditos
C=2
S=1
R=3
U=4
ingreso=int(input("por favor coloque su ingreso:  "))
nacimiento=int(input("por favor coloque su año de nacimiento:  "))
hijos=int(input("coloque su numero de hijos:  "))
pertenencia=int(input("coloque sus años de pertenencia al banco:  "))
estado_civil=(input("coloque su estado civil, aprete 1 si es soltero y 2 si es casado:  "))
vivienda=(input("¿vives en zona rural o urbana? coloca 3 si es rural y 4 si es urbana:   "))  
if pertenencia>10 and hijos>=10 and estado_civil == C and -nacimiento +2022<=55 and -nacimiento+2022>=45 and ingreso>2500000 and estado_civil is S and vivienda is U and ingreso>3500000 and pertenencia>5 and vivienda is R and estado_civil == 2 and hijos<2:
 print("APROBADO")
else:
  print("RECHAZADO")      