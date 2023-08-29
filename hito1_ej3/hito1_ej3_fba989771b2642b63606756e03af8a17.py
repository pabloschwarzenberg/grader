#Aprobación de créditos
ingreso=int(input("indique su ingreso mensual: "))
nacimiento=int(input("ingrese su año de nacimiento: "))
hijos=int(input("ingrese la cantidad de hijos: "))
banco=int(input("¿cuando años lleva en esta banco?: "))
civil=str(input("indique su estado civil: S para Soltero y C para casado: "))
lugar=str(input("indique lugar de alogamiento: U para Urbano y R para Rural: "))
C=1
S=2
R=3
U=4
if(banco>10 and hijos>=2):
  print("APROBADO")
elif(civil==1 and hijos>3 and 45>=2020-nacimiento<=55):
  print("APROBADO")
elif(ingreso>=2500000 and civil==2 and lugar==4):
  print("APROBADO")
elif(ingreso>=3500000 and banco>=5):
  print("APROBADO")
elif(lugar=="R" and civil=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")