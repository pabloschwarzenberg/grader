S=1
U=2
R=4
C=3
ingresos= eval(input("ingresos anuales"))
anacimiento= eval(input("ingrese su año de nacimiento"))
hijos= eval(input("¿cuantos hijos tiene?"))
pertenencia= eval(input("¿cuantos años lleva en el banco?"))
ec= eval(input("estado civil S o C"))
edad= 2020-anacimiento
vive= eval(input("vive en un ambiente U urbano o R rural"))
if ec==C and hijos>3 and 55>edad>45:
  print("APROBADO")
elif pertenencia>10 and hijos>=2:
  print("APROBADO")
elif ingresos>2500000 and ec==S and vive==U:
  print("APROBADO")
elif ingresos>3500000 and pertenencia>5:
  print("APROBADO")
elif vive==R and hijos<2 and ec==C:
  print("APROBADO")
else:
  print("RECHAZADO")