#Aprobación de créditos
ingresos         =int(input("ingreso en pesos?(sin puntos):"))

añonacimiento    =int(input("¿en que año nacio?:"))

ndehijos         =int(input("¿cuantos hijos tiene?:"))

añodepertenencia =int(input("¿cuantos años lleva en el banco?:"))

estadocivil      =input("estado civil?\n soltero(s)\n casado (c)\n : ")

campoociudad     =input("vive en campo o ciudad?\n urbano (u)\n rural(r)\n :")

if añodepertenencia > 10 and ndehijos >= 2:
    print("APROBADO")
elif estadocivil == "S" and ndehijos > 3 and añodepertenencia >= 1967 and añodepertenencia <= 1977:
    print("APROBADO")
elif ingresos > 2500000 and estadocivil == "S" and campoociudad == "U":
    print("APROBADO")
elif ingresos > 3500000 and añodepertenencia > 5:
    print("APROBADO")
elif campoociudad == "R" and ndehijos < 2 and estadocivil == "C":
    print("APROBADO")
else:print("rechazado")      