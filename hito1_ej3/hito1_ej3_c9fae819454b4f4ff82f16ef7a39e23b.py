#Aprobación de créditos
ingreso=int(input("ingrese el dinero en pesos:",))
nacimiento=int(input("ingrese su año de nacimiento:",))
hijos=int(input("ingrse su numero de hhijos:",))
bancoyears=int(input("ingrese cuantos años a estado en el banco:",))
estadocivil=input("ingrese su estado civil (S o C):",)
vivienda=input("ingrese donde vive (U o R)",)
edad=2020-nacimiento
if(bancoyears>=10 and hijos>=2):
    print("APROBADO")
elif(estadocivil=="C" and hijos>3 and edad>=45 and edad<=55):
    print("APROBDO")
elif(ingreso>2500000 and estadocivil==S and vivienda=="U"):
    print("APROBADO")
elif(ingreso>3500000 and bancoyears>5):
    print("APROBADO")
elif(vivienda=="R" and estadocivil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")