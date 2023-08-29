#Aprobacion de creditos
Ingreso = int(input("Ingrese, en pesos, sus ingresos: "))
Nacimiento = int(input("Ingrese su año de nacimiento: "))
Num_Hijos = int(input("Ingrese su numero de hijos: "))
Años_Banco = int(input("Ingrese la cantidad de años de pertenencia al banco: "))
Estado = str(input("Ingrese su estado civil es decir, soltero(S) o casado(C): "))
Vive = str(input("Ingrese si vive en zona rural(R) o en ciudad (U): "))

if Años_Banco > 10 and Num_Hijos >= 2:
    print("APROBADO")
elif Estado == "C" and Nacimiento > 1967 and Nacimiento < 1977:
    print("APROBADO")
elif Ingreso > 2500000 and Estado == "S" and Vive == "U":
    print("APROBADO")
elif Ingreso > 3500000 and Años_Banco > 5:
    print("APROBADO")
elif Vive == "R" and Estado == "C" and Num_Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")


      