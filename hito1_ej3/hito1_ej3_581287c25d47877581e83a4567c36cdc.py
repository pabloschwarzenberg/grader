ingreso=int(input("1200000"))
año=int(input("1972"))
hijos=int(input("2"))
años_banco=int(input("10"))
estado_civil=input("C")
vivienda=input("R")
edad=2020-año

if (años_banco>=10 and hijos>=2):
    print("APROBADO")
elif (estado_civil=="C" and hijos>>3 and 55>=edad>=45):
    print("APROBADO")
elif (ingreso>=2500000 and estado_civil=="S" and vivienda=="U"):
    print("APROBADO")
elif (ingreso>=3500000 and años_banco>=5):
    print("APROBADO")
elif (vivienda=="R" and estado_civil=="C" and hijos<=2):
    print("APROBADO")
else:
    print("RECHAZADO")
