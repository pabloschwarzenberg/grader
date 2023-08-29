#Aprobación de credito
ingreso = 0
aNacimiento = 0
nhijos = 0
aBanco = 0
estadoCivil = None
zona = None

ingreso = int(input("Indique ingresos:  $"))
aNacimiento = int(input("Año Nacimiento XX: "))
nhijos = int(input("Indique N° Hijos: "))
aBanco =int( input("Indique Años de Cliente: ") )
estadoCivil = input ("S: soltero, C, casado: ")
zona = input ("U: Urbano, R, Rural: ")



if((aBanco >= 10) and (nhijos >= 2)):
    print ("\n ESTADO: APROBADO")
elif((estadoCivil == "C") and (nhijos > 3) and ( (aNacimiento >= 45 ) and (aNacimiento <= 55) ) ) :
    print ("\n ESTADO: APROBADO")
elif((estadoCivil == "S") and (ingreso >= 2500000) and (zona =="U")):
    print ("\n ESTADO: APROBADO")
elif( (ingreso >= 3500000) and (aBanco >= 5)):
    print ("\n ESTADO: APROBADO")
elif ((estadoCivil == "C") and (nhijos < 2) and (zona == "R")):
    print ("\n ESTADO: APROBADO")
else:
    print("\n ESTADO: RECHAZADO")