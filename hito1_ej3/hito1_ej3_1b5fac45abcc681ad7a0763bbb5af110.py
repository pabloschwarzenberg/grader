#Aprobación de créditos
ingresos=int(input("Registre sus ingresos(en pesos chilenos): "))
nacimiento=int(input("Ingrese su año de nacimiento: "))
edad= 2022 - nacimiento
hijxs=int(input("Ingrese cuantos hijos tiene: "))
pertenencia=int(input("Ingrese los años que lleva perteneciendo al banco: "))
estado=int(input("Si está soltero ingrese S y si está casado ingrese C: "))
vive=input("Ingrese U si vive en ciudad y R si vive en campo: ")
if pertenencia>10 and hijxs>=2:
  print(APROBADO)
  elif estado == "C" and hijxs > 3 and edad > 45 and edad < 55:
   print(APROBADO)
  elif ingresos>2500000 and estado== S and vive== "U":
    print(APROBADO)
  elif ingresos>3500000 and pertenencia >5:
    print(APROBADO)
  elif vive == R and estado== C and hijxs<2:
    print(APROBADO)
 else:
   print(RECHAZADO)