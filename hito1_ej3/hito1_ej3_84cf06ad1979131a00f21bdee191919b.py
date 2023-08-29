#Aprobación de créditos

#Ingreso (en pesos)
Ingresos = int(input("Indique sus ingresos: "))
#Año de nacimiento
A_DeNacimiento = int(input("Ingrese su año de nacimiento: "))
#Número de hijos
N_DeHijos = int(input("Ingrese la cantidad de hijos: "))
#Años de pertenencia al banco
A_DePertenecia = int(input("Ingrese la cantidad de años que lleva en el banco: "))
#Estado civil ("S": soltero, "C", casado)
EstadoCivil = input("ingrese su estado civil (S:Soltero o C:Casado): ")
#Si vive en campo o cuidad ("U": urbano, "R": rural)
Ubicacion = input("Indique si vive en Campo o Ciudad(C:Campo , R:Rural): ")

#El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if A_DePertenecia>10 and  N_DeHijos>2:
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif EstadoCivil == "C" and N_DeHijos>3 and 1965<A_DeNacimiento<1975:
    print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif Ingresos>2500000 and EstadoCivil == "S" and Ubicacion == "R":
    print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif Ingresos>3500000 and A_DePertenecia>5:
    print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif Ubicacion == "R" and EstadoCivil == "C" and N_DeHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
#Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.