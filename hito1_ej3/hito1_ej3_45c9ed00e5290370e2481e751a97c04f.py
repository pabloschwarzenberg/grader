#Aprobación de créditos.

ingresos = int(input("Por favor indique su ingreso: "))
nacimiento = int(input("Por favor ingrese su año de nacimiento: "))
hijos = int(input("Por favor ingrese la cantidad de hijos que tiene: "))
anos_banco = int(input("Por favor ingrese sus años en el banco: "))
civil = str(input("Por favor ingrese su estado 'S' si es soltero o 'C' si es casado: "))
lugar = str(input("Por favor indique si vive en campo o zona rural 'R' o en la ciudad o zona urbana 'U': "))

ano_actual = (2021)
edad_actual = (ano_actual - nacimiento)
#print(edad_actual)
#print(ingresos)
#print(civil)
#print(lugar)
#Condiciones.

if anos_banco > 10 and hijos >= 2:
    condicion_1 = True
else:
    condicion_1 = False

if civil == "C" and hijos >= 3 and 45 <= edad_actual <= 55:
    condicion_2 = True
else:
    condicion_2 = False
    
if ingresos >= 2500000 and civil == "S" and lugar == "U":
    condicion_3 = True
else:
    condicion_3 = False
    
if ingresos >= 3500000 and anos_banco >= 5:
    condicion_4 = True
else:
    condicion_4 = False
    
if lugar == "R" and civil == "C" and hijos < 2:
    condicion_5 = True
else:
    condicion_5 = False

if condicion_1 or condicion_2 or condicion_3 or condicion_4 or condicion_5 == True:
    credito = True
    print("APROBADO")
else:
    credito = False
    print("RECHAZADO")

