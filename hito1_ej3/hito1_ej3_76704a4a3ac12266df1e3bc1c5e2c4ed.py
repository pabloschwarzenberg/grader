#Aprobación de créditos
ingreso=int(input("cuales son sus ingresos $: "))
años=int(input("ingrese su edad: "))
hijos=int(input("ingrese numero de hijos: "))
años_en_banco=int(input("ingrese numero de años en el banco: "))
estado_civil=str(input("ingrese S si esta soltero o C si esta casado: "))
S="soltero"
C="casado"
casa=str(input("ingrese U si vive la ciudad o R si vive en el campo: "))
U="ciudad"
R="campo"
if años_en_banco>10 and hijos>=2:
  print("APROBADO")
elif estado_civil<S and hijos>3 and 45<años<55:
  print("APROBADO")
elif ingreso>2500000 and estado_civil>C and casa>R:
  print("APROBADO")
elif ingreso>3500000 and años_en_banco>5:
  print("APROBADO")
elif casa<U and estado_civil<S and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")