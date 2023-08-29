#Aprobación de créditos
i=int(input("indique sus ingresos:"))
nacimiento=int(input("año de nacimiento:"))
nh=int(input("número de hijos:"))
banco=int(input("años perteneciente al banco:"))
c=input("¿estado civil?, ¿casado(C) o soltero(S)?:")
ciudad=input("vive en campo(R) o ciudad(U):")
actualidad=2018
edad= actualidad-nacimiento

if banco>10 and nh>=2:
  print("APROBADO")
elif c=="C" and nh>3 and edad>=45 and edad<=55:
  print("APROBADO")
elif i>3500000 and banco>5:
  print("APROBADO")
elif i>2500000 and c=="S" and ciudad=="U":
  print("APROBADO")
elif ciudad=="R" and c=="C" and nh<2:
  print("APROBADO")
else:
  print("RECHAZADO")      