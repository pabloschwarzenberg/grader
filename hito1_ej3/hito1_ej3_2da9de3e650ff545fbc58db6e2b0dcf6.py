#Aprobación de créditos
ingreso=int(input("cual es su ingreso(en pesos)? "))
an=int(input("ingrese su año de nacimiento: "))
nh=int(input("cuantos hijos tiene?: "))
aps=int(input("ingrese el año de ingreso al banco: "))
ec=(input("ingrese su estado civil(s/c):"))
vive=input("donde vive? [r(rural)/u(urbano]")
edad=2022-an
aeb=2022-aps

if (aps>=10 and nh>=2):
  print("APROBADO")

elif (ec=="c" and nh>=3 and (edad>=45 or edad<=55)):
  print("APROBADO")

elif (ingreso>=2500000 and ec=="s" and vive=="u"):
  print("APROBADO")

elif (ingreso<=3500000 and aeb>5):
  print("APROBADO")

elif (vive=="r" and (ec=="c" or ec=="C") and nh>2):
  print("APROBADO")

else:
  print("RECHAZADO")