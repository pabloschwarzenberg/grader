#Aprobación de crédito
ingreso=eval(input("Introduzca sus ingresos en pesos: "))
nacimiento=int(input("Introduzca su año de nacimiento: "))
nhijos=int(input("Introduzca la cantidad de hijos: "))
aniobanco=eval(input("Introduzca la cantidad de años que pertenece al banco: "))
civil=str(input("Introduzca su estado civil (casada(o): C, soltera(o): S): "))
vivienda=str(input("Introduzca si vive en área urbana o rural (Urbana: U, Rural: R): "))

edad= 2022 - nacimiento

if aniobanco>10 and nhijos >=2:
  print("APROBADO")
elif civil =="C" and nhijos>3 and 45<edad<55:
  print("APROBADO")
elif ingreso>2500000 and (civil=="S" or civil=="s") and (vivienda=="U" or vivienda=="u"):
  print("APROBADO")
elif ingreso>3500000 and aniobanco>5:
  print("APROBADO")
elif (vivienda=="R" or vivienda=="r") and (civil=="C" or civil=="c") and nhijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")
  
