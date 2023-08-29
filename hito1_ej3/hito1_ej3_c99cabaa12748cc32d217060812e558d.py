#Aprobación de créditos
# Valor Constante
AnioActual=2020
FlagAprobado = 0

# Variables de ingreso cliente
Ingresos=int(input("Ingreso: "))
AnioNacimiento=int(input("Anio Nacimiento: "))
NunmeroHijos=int(input("Numero Hijos: "))
AniosBanco=int(input("Anios en el banco: "))
EstadoCivil=input("(S: soltero, C, casado):")
Residencia=input("(U: urbano, R: rural):")

#Calculo de edad
AniosCliente=2020-AnioNacimiento

#Logica del Banco
if AniosBanco >= 10 and NunmeroHijos >= 2:
    FlagAprobado = 1
if EstadoCivil == "C" and NunmeroHijos >= 3 and (AniosCliente>=45 and AniosCliente<=55):
    FlagAprobado = 1
if Ingresos >= 2500000 and EstadoCivil == "S" and Residencia == "U":
    FlagAprobado = 1
if Ingresos >= 3500000 and AniosBanco >=5:
    FlagAprobado = 1
if Residencia == "R" and EstadoCivil == "C" and NunmeroHijos <= 2:
    FlagAprobado = 1
    
#Resultado    
if FlagAprobado == 1:
    print("APROBADO")
else:
    print("RECHAZADO")