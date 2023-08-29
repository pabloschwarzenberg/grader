#Aprobación de créditos
INGRESOS = int(input("Total de Ingresos: "))
ANIO_NACIMIENTO = int(input("Ingrese su año de nacimiento: "))
NUM_HIJOS = int(input("Cantidad de hijos: "))
ANIOS_BANCO = int(input("Cantidad de años que pertenece nuestro banco: "))
ESTADO_CIVIL = str(input("Si está casado ingrese una C, Si está soltero ingrese una S: "))
RESIDENCIA = str(input("Si reside en el campo ingrese una R, Si reside en la ciudad ingrese una U: "))

if ANIOS_BANCO > 10 and NUM_HIJOS >= 2:
   print("APROBADO")
if ESTADO_CIVIL == "C" and NUM_HIJOS > 3 and ANIO_NACIMIENTO > 1966 and ANIO_NACIMIENTO < 1976:
   print("APROBADO")
if INGRESOS > 2500000 and ESTADO_CIVIL == "S" and RESIDENCIA == "U":
   print("APROBADO")
if INGRESOS > 3500000 and ANIOS_BANCO > 5:
   print("APROBADO")
if RESIDENCIA == "R" and ESTADO_CIVIL == "C" and NUM_HIJOS < 2:
   print("APROBADO")
else:
   print("RECHAZADO")