#Aprobación de créditos
ingreso= int(input("Ingrese sus ingresos mensuales: "))
ano=int(input("Ingrese su año de nacimiento: "))
numH= int(input("Ingrese su numero de hijos: "))
anosB= int(input("Ingrese los años que lleva como cliente"))
estadoC=str(input("Cual es su estado civil (S o C): "))
lugar= str(input("¿Usted vive en campo o ciudad? (U o R)"))

edad=2021-ano



if anosB>=10 and numH>=2:
    print("APROBADO")

elif estadoC=="C" and numH>=3 and edad>=45 and edad<=55:
    print("APROBADO")

elif ingreso>=250000 and estadoC=="S" and lugar=="U":
    print("APROBADO")

elif ingreso>=350000 and anosB>=5:
    print ("APROBADO")

elif lugar=="R" and estadoC=="C" and numH<=2:
    print("APROBADO")

else:
    print("RECHAZADO")     