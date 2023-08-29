#Aprobación de créditos
Ingreso=int(input("Ingrese sus ingresos en pesos chilenos($): "))
año=int(input("Ingrese su año: "))
hijos=int(input("Ingrese su cantidad de hijos: "))
banco=float(input("Ingrese los años de pertenencia en el banco: "))
Civil=input("Ingrese su estado civil: ")
hogar=input("Ingrese si vive en Campo o Ciudad: ")
C="casado/a"
S="solero/a"
U="Urbano"
R="Rural"
if banco>10 and hijos>=2:
  print("APROBADO")
else:
   if Civil=="C" or Civil=="c" and hijos>3 and año>=45 and año<=55:
    print("APROBADO")
   else:
    if Ingreso>2500000 and Civil=="S" or Civil=="s" and hogar=="U"or hogar=="u":
     print("APROBADO")
    else:
     if Ingreso>3500000 and banco>5:
      print("APROBADO")
     else:
      if hogar=="R" or hogar=="r" and Civil=="C" or Civil=="c" and hijos<2 and hijos>1:
       print("APROBADO")
      else:
       print("RECHAZADO")    