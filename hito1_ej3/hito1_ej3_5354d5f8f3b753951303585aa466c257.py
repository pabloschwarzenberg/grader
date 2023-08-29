ingresos=(int(input("Ingrese su Renta Mnesual ")))
ano=(int(input("Ingrese su Año de Nacimiento ")))
nh=(int(input("Ingrese cantidad de Hijos ")))
ano_bco=(int(input("Ingrese los Años como cliente del Banco ")))
ec=(input("Ingrese su estado Civil S=Soltero, C=Casado " ))
area=(input("Ingrese su Area de Residencia U=Urbano, R=Rural) "))
if ano_bco>10 and nh>=2:
  print("APROBADO")
if ec=="C" and nh>3 and 2022-ano>=45 and 2022-ano<=55 :
  print("APROBADO")
if ingresos>2500000 and ec=="S" and area=="U" :
  print("APROBADO")
if ingresos>3500000 and ano_bco>5:
  print("APROBADO")
if area=="R" and ec=="C" and nh<2:
  print("APROBADO")