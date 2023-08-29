ingreso=eval(input("Indique sus ingresos:"))

edad=eval(input("Indique su edad:"))
hijos=eval(input("Indique el numero de hijos que tiene:"))
años_banco=eval(input("Indique la cantidad de años que lleva en el banco:"))
estado_civil=str(input("Indique si es soltero(S) o casado(C):"))
vivienda=str(input("Indique si vive en zona urbana(U) o rural(R):"))

if años_banco >=10 and hijos >=2:
    print("APROBADO")
elif estado_civil == "C" and hijos >=3 and 45>= edad <=55:
    print("APROBADO")
elif ingreso>2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso>3500000 and años_banco >=5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos <=2:
    print("APROBADO")
else:
    print("RECHAZADO")


