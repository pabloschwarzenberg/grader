#Aprobación de créditos     
ingreso = int(input("Mencione su ingreso en pesos\n"))
ano_nascimiento = int(input("Mencione su ano de nascimiento\n"))
numero_hijos = int(input("Cuantos hijos tiene?\n"))
pertenencia_banco = int(input("Cuantos anos lleva con nosotros?\n"))
estado_civil = str(input("(s: soltero, c: casado)\n"))
sector = str(input("(u:urbano, r:rural)\n"))
edad = 2020 - ano_nascimiento 

if pertenencia_banco > 10 and numero_hijos >=2 :
  print("APROBADO")
elif pertenencia_banco > 5 and ingreso < 3500000 :
  print("APROBADO")
elif numero_hijos > 3 and 45 <= edad <= 55 and estado_civil == "c" :
  print("APROBADO")
elif numero_hijos < 2 and estado_civil == "c" and sector == "r" :
  print("APROBADO")
elif sector == "u" and estado_civil == "s" and ingreso > 2500000 :
  print("APROBADO")
else: 
  print("RECHAZADO")