monto=int(input("Ingreso (en pesos):"))
anodenacimiento=int(input("Año de nacimiento"))
Numerodehijos=int(input("numero de hijos:"))
anosEnBanco=int(input("Años de pertenencia al banco"))
estadocivil=input("Estado civil S: soltero C casado:")
vivienda=input("Si vive en campo o cuidad ("U": urbano, "R": rural):")

var1="APROBADO"
var2="RECHAZADO"
edad=anodenacimiento-2018
if anosEnBanco<10 and Numerodehijos>=2:
    print(var1)
elif estadocivil== "c" and Numerodehijos>3 and  edad <55 and edad >45:
    print(var1)
elif monto >=250000 and estadocivil == "s" and vivienda == "r":
    print(var1)
elif monto >=250000 and anosEnBanco > 5:
    print(var1)
elif estadocivil == "c"and vivienda == "u"and Numerodehijos>=2 :
    print(var1)
else:
    print(var2)