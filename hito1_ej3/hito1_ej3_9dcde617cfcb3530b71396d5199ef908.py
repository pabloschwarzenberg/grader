#Aprobación de créditos
i= eval(input("ingrese su ingreso en pesos chilenos: "))
a= eval(input("ingrese su año de nacimiento: "))
h= eval(input("ingrese cuantos hijos tiene: "))
ab= eval(input("ingrese cuantos años lleva en el banco:"))
e= (input("si es soltero ingrese S , si es casado ingrese C : "))
cas= str("C")
s= str("S")
l= (input("si vive en campo ingrese R si vive en ciudad ingrese U: "))
c= str("U")
ca= str("R")
if ab > 10 and h > 2:
  print("APROBADO")
if e == cas and h > 3 and a <= 1966 and a >= 1956:
  print("APROBADO")
if i > 2500000 and e == s and l == c:
  print("APROBADO")
if i > 3500000 and ab > 5:
  print("APROBADO")
if l == ca and e == cas and h < 2:
  print("APROBADO")
else:
  print("RECHAZADO")