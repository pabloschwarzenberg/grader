#Aprobación de créditos
ingreso = int(input("ingrese su capital:"))
nacimiento = int(input("ingrese su año de nacimiento:"))
hijos = int(input("ingrese cuantos hijos tiene:"))
tiempoconelbanco = int(input("ingrese cuantos años lleva con el banco:"))
estcivil = str(input("ingrese su estado civil, (S) si es soltero o (C) si es casado:"))
vivienda = str(input("ingrese la zona donde vive, (R) si es en el campo, (U) si es en la ciudad;"))

actualidad = 2021
edad = actualidad-nacimiento

if tiempoconelbanco>10 and hijos>=2:
 print("APROBADO")

if str(estcivil)=="C" and hijos>3 and edad>45 and edad<55:
 print("APROBADO")

if ingreso>2500000 and str(estcivil)=="S" and str(vivienda)=="U":
 print("APROBADO")

if ingreso>3500000 and tiempoconelbanco>5:
 print("APROBADO")

if str(vivienda)=="R" and str(estcivil)=="C" and hijos<2:
 print("APROBADO")