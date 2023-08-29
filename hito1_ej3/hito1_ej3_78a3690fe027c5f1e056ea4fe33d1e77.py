#Aprobación de créditos
#Entrada de datos
ingreso = int(input("Ingrese su ingreso mensual: $"))
añoNacimiento = int(input("Ingrese su año de nacimiento: "))
nroHijos = int(input("Ingrese el numero de hijos que ud tenga: "))
añoAntiguedad = int(input("Ingrese los años de pertenencia al banco: "))
estadoCivil = str(input("Ingrese su Estado civil ((S): Soltero, (C): Casado)"))
residencia = str(input("Ingrese si vive en campo o en ciudad ((U): Urbano, (R): Rural)"))
resultado = ""
#Procesamiento de datos
if añoAntiguedad >= 10 and nroHijos >= 2:
    resultado = "APROBADO"
if estadoCivil == "C" and nroHijos > 3 and 1965 <= añoNacimiento >= 1975:
    resultado = "APROBADO"
if ingreso > 2500000 and estadoCivil == "S" and residencia == "U":
    resultado = "APROBADO"
if ingreso > 3500000 and añoAntiguedad >= 5:
    resultado = "APROBADO"
if residencia == "R" and estadoCivil == "C" and nroHijos < 2:
    resultado = "APROBADO"
if resultado != "APROBADO":
    resultado = "RECHAZADO"

#Salida de datos
print(resultado)