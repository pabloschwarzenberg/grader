#Aprobación de créditos
ingreso=int(input("ingrese sus ingresos en pesos:",))
nacimiento=int(input("ingrese su año de nacimiento:",))
hijos=int(input("ingrese su numero de hijos:",))
años=int(input("ingrese el numero de años que a lleba en el banco:"))
civil=input("ingrese su estado civil:")
vivienda=input("ingrese donde vive,("U" para urbano,"R" para rural):")
edad=2020-nacimiento
C=1
S=2
U=3
R=4
if(años>10 and hijos>2):
    print("APROBADO")
elif(civil==1 and hijos>3 and edad>45 and edad<55):
    print("APROBADO")
elif(ingreso>250000 and civil==2 and vivienda==3):
    print("APROBADO")
elif(ingreso>350000 and años>5):
    print("APROBADO")
elif(vivienda==4 and civil==1 and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")