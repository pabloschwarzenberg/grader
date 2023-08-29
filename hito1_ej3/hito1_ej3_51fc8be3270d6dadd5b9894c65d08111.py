ingreso = int(input("Mencione su ingreso en pesos\n"))
año_nacimiento = int(input("Mencione su año de nacimiento\n"))
numero_hijos = int(input("¿Cuantos hijos tiene?\n"))
pertenencia_banco = int(input("¿cuantos años lleva con nosotros?\n"))
estado_civil = str(input("(S: soltero, C: casado)\n"))
sector = str(input("(U: urbano, R: rural)\n"))
edad= 2020 - año_nacimiento

if pertenencia_banco>10 and numero_hijos>=2:
  print("APROBADO")
elif pertenencia_banco>5 and ingreso>3500000:
  print("APROBADO")    
elif numero_hijos>3 and 45<=edad<=55 and estado_civil =="C":
  print("APROBADO") 
elif numero_hijos<2 and estado_civil=="C" and sector=="R" :
  print("APROBADO")
elif sector=="U"and estado_civil=="S" and ingreso >2500000:
  print("APROBADO")
else:
 print("RECHAZADO")   