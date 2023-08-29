#Aprobación de créditos
ingresos=int(input("ingrese ingresos"))
nacimineto=int(input("ingrese fecha de nacimineto"))
hijos=int(input("ingrese numero de hijos"))
pertenecia=int(input("hace cuantos años pertenece al banco"))
casadosoltero=str(input("es casado o soltero"))
zona=str(input("rural o urbano"))
c=7
s=3
r=12
u=14
if(pertenecia>10 and hijos>=2):
  print("APROBADO")
if(casadosoltero==7 and hijos>3 and nacimiento==1975>=1955):
  print("APROBADO")
if(ingresos>2500000 and casadosoltero==3 and zona==12):
  print("APROBADO")
if(ingresos>3500000 and pertenecia>5):
  print("APROBADO")
if(zona=="R" and casadosoltero=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")
print(zona)
print(casadosoltero)
print(hijos)