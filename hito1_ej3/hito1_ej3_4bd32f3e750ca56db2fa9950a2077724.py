#Aprobación de créditos
S=1
C=0
U=1
R=0
ingreso= eval(input("ingreso en pesos: "))
año= eval(input("año de nacimiento: "))
hijos= eval(input("ingrese el numero de hijos: "))
anosBanco= eval(input("ingrese años pertenencia al banco"))
EC= eval(input("es solero o casado S/C: "))
vive= eval(input("donde vive urbano o rural U/R: "))
if anosBanco >10 and hijos >= 2:
  print("APROBADO")
elif EC==0 and hijos >3 and (2020-año)> 45 and (2020-año)<=55:
  print("APROBADO")
elif ingreso>2500000 and EC ==1 and vive== 0:
  print("APROBADO")
elif ingreso > 3500000 and anosBanco> 5:
  print("APROBADO")
elif vive==0 and EC==0 and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")