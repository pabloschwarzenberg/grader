#Aprobación de créditos
## ENTRADA DE DATOS - PROCESO - SALIDA DE DATOS

Ingreso = float(input("Digite su ingreso mensual:  "))
Año_Nacimiento = int(input("Ingrese su Año de Nacimiento: "))
Número_hijos = int(input("Ingrese Número de hijos: "))
Antiguedad_Banco = int(input("Ingrese cantidad de años en el Banco: "))
Estado_Civil = input("Ingrese Estado Civil(S: Soltero, C: Casado):")
Sector_Domicilio = input("Ingrese sector (U: Urbano, R: Rural):")

if Antiguedad_Banco >= 10 and Número_hijos >= 2:
    print("APROBADO")   
elif Estado_Civil == "C" and Número_hijos > 3 and Año_Nacimiento >= 1968 and Año_Nacimiento <= 1978:
    print("APROBADO")
elif Ingreso > 2500000 and Estado_Civil == "S" and Sector_Domicilio == "U":
    print("APROBADO")
elif Ingreso > 3500000 and Antiguedad_Banco > 5:
    print("APROBADO")
elif Sector_Domicilio == "R" and Estado_Civil == "C" and Número_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")