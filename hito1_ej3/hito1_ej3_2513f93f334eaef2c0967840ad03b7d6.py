ingreso=eval(input("ingrese sus ingresos"))
nacimiento=eval(input("ingrese su año de nacimiento"))
hijos=eval(input("ingrese cuantos hijos tiene"))
años=eval(input("ingrese años de pertenencia al banco"))
estado=str(input("ingrese su estado civil(C o S"))
vivienda=str(input("ingrese si vive en campo(R) o ciudad(U)"))
edad=2020-nacimiento
if (años>=10 and hijos>=2):
 print("APROBADO") 
elif(estado=="C" and hijos>=3 and edad>=45 and edad<=55):
 print("APROBADO") 
elif(ingreso>=250000 and estado=="S"and vivienda=="U"):
  print("APROBADO")
elif(ingreso>=350000 and años>=5):
  print("APROBADO")
elif(vivienda=="U" and estado=="C" and hijos<=1 ):
 print("APROBADO")
else:
  print("RECHAZADO")
     