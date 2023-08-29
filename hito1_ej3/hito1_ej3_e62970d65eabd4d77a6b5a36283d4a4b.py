ingreso = int(input("Ingrese el ingreso mensual"))
anio = int(input("Ingrese el año de nacimiento"))
numHijos = int(input("Ingrese el número de hijos"))
anioBanco = int(input("Ingrese los años en el banco"))
estadoCivil = input("Estado Civíl")
localidad = input("ingrese Urbano (U) o Rural (R)")


if(anioBanco>10 and numHijos >= 2):
    print("APROBADO")

elif(estadoCivil=="C" and numHijos > 3 and anio < 1976 and anio >1966):
    print("APROBADO")

elif(ingreso>2500000 and estadoCivil == "S" and localidad == "U"):
    print("APROBADO")

elif(ingreso>3500000 and anioBanco >5):
    print("APROBADO")

elif(localidad == "R" and estadoCivil == "C" and numHijos <2):
    print("APROBADO")

print("RECHAZADO")