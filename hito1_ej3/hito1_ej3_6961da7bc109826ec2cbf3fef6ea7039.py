#Aprobación de créditos
print("SISTEMA PARA VERIFICAR REQUISITOS CLIENTE BANCARIO")

ingresos = int(input("Ingrese sus ingresos mensuales en pesos: "))
fecha = input("ingrese su año de nacimiento: ") 

hijos = int(input("ingrese el número de hijos que tiene: "))
pertenenciaalbanco = int(input("ingrese los años que lleva de cliente en el banco: "))
ecivil = input("Indique el documento S (soltero) o C (casado) : ")
ambito = input("Indique el documento U (urbano) o R (rural) : ")

puntos = 0

# Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.

if pertenenciaalbanco > 10 and hijos >= 2:
    puntos = puntos + 1
print("mensaje")

# Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.

if ecivil = C and hijos > 3 and 1966 < fecha < 1976:
    puntos = puntos + 1
print("Mensaje")

# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.

if ingresos > 2500000 and ecivil = S and ambito = U:
    puntos = puntos + 1
print("Mensaje")

# Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años

if ingresos > 3500000 and pertenenciaalbanco > 5:
    puntos = puntos + 1
print("Mensaje")

# Si el cliente vive en el campo, es casado y tiene menos de dos hijos.

if ambito = R and ecivil = C and hijos < 0:
    puntos = puntos + 1
print("Mensaje")

if puntos >= 2:
    print("Aprobado")
else:
    print("Rechazado")      