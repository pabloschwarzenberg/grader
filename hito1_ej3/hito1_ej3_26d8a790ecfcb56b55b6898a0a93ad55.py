#Matías
money=int(input("Ingresos que recibe: ", ))
year=int(input("Ingrese en que año nacio: ", ))
edad=int(2020-year)
kid=int(input("Ingrese la cantidad de hijos: ", ))
if (kid<0):
  print("ingreso mal los datos")
Year=int(input("Cantidad de años que lleva en el banco: ", ))
estado=input("Si usted esta soltero escriba'S', si esta casado escriba 'C': ", )
C=float(1)
Casado= C
S=float(2)
Soltero= S
R=float(3)
Rural=R
U=float(4)
Urbano=U
if (estado == S) or (estado == C):
   print(estado)
viv=input("Si usted vive en zona rural escriba 'R', si vive en cuidad coloque 'U': ", )
if (C) and (R) and (kid<2):
   print("APROBADO")
elif(S and (kid > 3) and (edad <= 55)and (45 <= edad)):
   print("APROBADO")
elif((year>=10) and (kid>=2)):
   print("APROBADO")
elif((money>2500000) and (S) and (U)):
   print("APROBADO")
elif((money>3500000)) and (Year>5):
  print("APROBADO")   
else:
   print ("RECHAZADO")