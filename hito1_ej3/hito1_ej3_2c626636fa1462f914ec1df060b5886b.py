ingreso = int(input("Ingrese el valor correspondiente a sus ingresos: $"))
año = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese el número de hijos:"))
años_banco = int(input("Ingrese los años que lleva en el banco:"))
estado = str(input("Ingrese su estado Civil (S si es soltero; C si es casado):"))
casa = str(input("¿Vive en campo o ciudad? Ingrese la letra U si es en ciudad, y R si es en el campo:"))
año_nac = 2020-año

if años_banco>=10 and hijos>=2:
    print("APROBADO")
elif estado=='C' and hijos>=3 and año_nac>=45 and año_nac<=55:
    print("APROBADO")
elif ingreso>= 2500000 and estado=='S'and casa=='U':
    print("APROBADO")
elif ingreso>=3500000 and años_banco>=5:
    print("APROBADO")
elif casa=='R' and estado=='C' and hijos<=2:
    print("APROBADO")
else: print("RECHAZADO")