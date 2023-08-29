#Aprobacion de creditos

ANIO_ACTUAL = 2020
ANIO = 0
Estado= ""
INGRESOS = int(input("Registre ingreso (en pesos): "))
ANIO_NAC = int(input("Ingrese año de nacimiento: "))
N_HIJOS = int(input("Ingrese cantidad de hijos: "))
ANIO_PERTENENCIA = int(input("Ingrese años de pertenencia al banco: "))
ESTADO_CIVIL = input("Ingrese estado civil (S: Soltero, C: Casado): ")
LUGAR_RESIDENCIA = input("Ingresar si vive en el campo o ciudad (U: urbano, R: rural): ")

if ANIO_NAC <= ANIO_ACTUAL:
    #ANIO = ANIO + 1
    CANTIDAD_ANIOS = ANIO_ACTUAL - ANIO_NAC
#print ("Cantidad de Anios: " + str(CANTIDAD_ANIOS))

if LUGAR_RESIDENCIA == "R" and ESTADO_CIVIL == "C" and N_HIJOS < 2:
    Estado="APROBADO"
elif ANIO_PERTENENCIA > 10 and N_HIJOS >= 2:
    Estado="APROBADO"
elif ESTADO_CIVIL == "C" and N_HIJOS > 3 and CANTIDAD_ANIOS <= 55 and CANTIDAD_ANIOS >= 45:
    Estado="APROBADO"
elif INGRESOS >= 2500000 and ESTADO_CIVIL == "S" and LUGAR_RESIDENCIA == "U":
    Estado="APROBADO"
elif INGRESOS > 3500000 and ANIO_PERTENENCIA > 5:
    Estado="APROBADO"
else:
    Estado="RECHAZADO"


print("El estado es :",Estado)
