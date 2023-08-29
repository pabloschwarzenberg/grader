#Aprobación de créditos
ingresos=int(input("¿Cuáles son sus ingresos mensuales?: $"))
año=int(input("¿En qué año nació?: "))
hijos=int(input("¿Cuántos hijos tiene?: "))
añosbanco=int(input("¿Cuántos años lleva usted en este banco?: "))
estado=str(input("¿Usted es una persona casada o soltera? C--> Casado S--> Soltero: "))
vivienda=str(input("¿Usted vive en el campo o en la ciudad? U--> Urbano(ciudad) R--> Rural(campo): "))
if añosbanco > 10 and hijos >= 2:
  print("APROBADO")
elif estado.upper () == "C" and hijos > 3 and 45<2022-año<55:
  print("APROBADO")
elif ingresos > 2500000 and estado.upper()== "S" and vivienda.upper()=="U":
  print("APROBADO")
elif ingresos > 3500000 and añosbanco > 5:
  print("APROBADO")
elif vivienda.upper()=="R" and estado.upper()=="C" and hijos< 2:
  print("APROBADO")
else:
  print("RECHAZADO")      