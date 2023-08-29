#Aprobación de créditos
ingresos=int(input("Digite sus ingresos en pesos: "))
ano_nacimiento=int(input("Ingrese su año de nacimiento: "))
edad=2022-ano_nacimiento
hijos=int(input("Ingrese cuantos hijos tiene: "))
anos_banco=int(input("Ingrese los años que lleva en el banco: "))
S="soltero"
C="casado"
print("S-soltero")
print("C-casado")
estado_civil=input("Indique su estado civil: ")
U="urbano"
R="rural"
print("U-urbano")
print("R-rural")
donde_vive=input("Ingrese donde reside: ")

if anos_banco>10 or hijos>=2:
  print("APROBADO")
elif estado_civil==C or hijos>3 or edad>= 45 and edad<=55:
  print("APROBADO")
elif ingresos>2500000 or estado_civil==S or donde_vive==U:
  print("APROBADO")
elif ingresos>3500000 or anos_banco>5:
  print("APROBADO")
elif donde_vive==R or estado_civil==C or hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")