#Aprobación de créditos
ingresos = int(input("Diga sus ingresos: ")) 
nacimiento = int(input("Diga su año de nacimiento: ")) 
hijos = int(input("Diga cuantos hijos tiene: ")) 
pertenencia = int(input("Diga cuantos años de pertenencia tiene al banco: ")) 
estado = input("Diga su estado civil ('S': Soltero,'C': Casado): ") 
localidad = input("Diga si vive en campo o cuidad ('U': urbano, 'R': rural): ")
edad = 2022-nacimiento

if pertenencia > 10 and hijos >= 2 :
  print("APROBADO")
elif estado == "C" and hijos > 3 and edad >= 45 and edad <= 55 :
  print("APROBADO")
elif ingresos > 2500000 and estado == "S" and localidad == "U" :
  print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5 :
  print("APROBADO")
elif localidad == "R" and estado == "C" and hijos < 2 :
  print("APROBADO")
else:
  print("RECHAZADO")