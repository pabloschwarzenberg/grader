#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos:"))
ano_nac = int(input("Ingrese su año de nacimiento:"))
num_hijos = int(input("Ingrese su número de hijos:"))
anos_pert = int(input("Ingrese cuantos años lleva de pertenencia en nuestro banco:"))
estado = input("Ingrese su estado civil ('S':Soltero,'C':Casado):")
vive = input("Ingrese si vive en campo o ciudad ('U':Urbano,'R':Rural):")
edad = 2021 - ano_nac
if anos_pert >10 and num_hijos >= 2:
  credito = "APROBADO"
elif ingreso >= 250000 and estado == 'S' and vive == 'U':
  credito = "APROBADO"
elif anos_pert > 5 and ingreso >= 350000:
  credito = "APROBADO"
elif num_hijos < 2 and estado == 'C' and vive == 'R':
  credito = "APROBADO"
elif  edad >= 45 and edad <= 55 and num_hijos > 3 and estado == 'C':
  credito = "APROBADO"
else:
  credito = "RECHAZADO"
print(credito)