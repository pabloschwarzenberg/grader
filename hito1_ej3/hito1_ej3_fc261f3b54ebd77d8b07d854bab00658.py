P=int(input("ingrese su ingreso en pesos:"))
N=int(input("ingrese su año de nacimiento:"))
H=int(input("ingrese su numero de hijos:"))
B=int(input("ingrese cuantos anos lleva en el banco:"))
E=input("ingrese c si usted esta casado y s si esta soltero:")
Z=input("ingrese U si usted vive en una zona urbana y R en una rural:")
if B >=10 and H >=2:
  print("APROBADO")
if E =="C"and H > 3 and N ==range(1967,1976):
  print("APROBADO")
if P> 2500000 and E =="S"and Z =="U":
  print("APROBADO")
if P>3500000 and B>5:
  print("APROBADO")
if Z =="R"and E =="C"and H<2:
  print("APROBADO")