#Aprobacion de creditos

Ingresos = int(input("Introduzca sus ingresos >>> "))

Nacimiento = int(input("Introduzca su fecha de nacimiento >>> "))

Hijos = int(input("Ingrese la cantidad la cantidad de hijos que tenga >>> "))

Pertenencia_Banco = int(input("Cuantos anos lleva perteneciendo a este banco? >>> "))

EstadoCivil = input("Usted es casado o soltero? >>>")

Hogar = input("Usted reside en un lugar urbano o rural?("U":Urbano,"R":Rural) >>> ")



AniosCliente = Nacimiento - 2022

if Pertenencia_Banco > 10 and Hijos >= 2:
    print("APROBADO")

elif EstadoCivil == "F" and Hijos > 3 and AniosCliente is range(45,55):
    print("APROBADO")

elif Ingresos > 2500000 and EstadoCivil == "C" and Hogar == "S":
    print("APROBADO")

elif Ingresos > 3500000 and Pertenencia_Banco > 5:
    print("APROBADO")

elif Hogar == "R" and Hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")