#credito bancario
i=float(input("cual es su ingreso en $:"))
a=int(input("año de nacimnieto:"))
n=int(input("Numero de hijos:"))
p=float(input("cuantos años lleva en este banco:"))
e=(input("marque (s) si es soltero o marque (c)si es casado:"))
h=(input("marque (u) si usted vive en la ciudad o marque (r) si usted vive en sector rural:"))
s=("soltero")
c=("casdo")
u=("ciudad")
r=("rural")
x= abs(a-2020)
if (p)>=10 and (n)>=2 :
  print("aprobado")
elif(x)>=45 and (x)<=55 and (e)==(c) and (n)>3:
  print("aprobado")
elif (i)>250000 and (h)==(u) :
  print("aprobado")
elif(i)>=350000 and (p)>5 :
  print("aprobado")
elif (h)==(r) and (e)== (c) and (n)<2 : print("aprobado")
else:
  print("rechazado")
  
