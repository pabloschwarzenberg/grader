#Aprobación de créditos
#atencion automatica de creditos de consumo

ingresos=int(input("Anote sus ingresos mensuales: $ "))
nacimiento = int(input("Ingrese su año de nacimiento"))
nHijos=int(input("Si tiene hijos ingrese la cantidad"))
antiguedadBanco=int(input("Hace cuantos años pertence al banco"))
estadoCivil=str(input("Estado civil S= soltero - C= Casado"))
lugarResidencia=str(input("Ingrese si vive en el campo o en la ciudad U = Urbano o R = Rural"))

if antiguedadBanco>10 and nHijos>=2:
    print("APROBADO")
elif estadoCivil=='C' and nHijos>3 and 2021-nacimiento>=45 and 2021-nacimiento<55:
    print("APROBADO")
elif ingresos>2500000 and estadoCivil=='S' and lugarResidencia=='U':
    print("APROBADO")
elif ingresos>3500000 and antiguedadBanco>5:
    print("APROBADO")
elif lugarResidencia=='R' and estadoCivil=='C' and nHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
     