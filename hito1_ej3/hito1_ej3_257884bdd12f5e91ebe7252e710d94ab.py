# INFORMACION POSTULANTES
AñoActual = 2021
Ingreso = int(input("monto en pesos: "))
AñoDeNacimiento = int(input("año de nacimiento: "))
Edad = (AñoActual) - (AñoDeNacimiento)
NumeroDeHijos = int(input("numero de hijos: "))
AñosDePertenenciaAlBanco = int(input("años pertenencia al banco: "))
EstadoCivil = str(input("soltero (S), casado (C): "))
ViveEn = str(input("urbano (U), rural (R): "))
# APROBADO O RECHAZADO
if AñosDePertenenciaAlBanco > 10 and NumeroDeHijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
if str(EstadoCivil) == "C" and NumeroDeHijos > 3 and Edad > 45 and Edad < 55:
    print("APROBADO")
else:
    print("RECHAZADO")
if Ingreso > 2500000 and str(EstadoCivil) == "S" and str(ViveEn) == "U":
    print("APROBADO")
else:
    print("RECHAZADO")
if Ingreso > 3500000 and AñosDePertenenciaAlBanco > 5:
    print ("APROBADO")
else:
    print("RECHAZADO")
if str(ViveEn) == "R" and str(EstadoCivil) == "C" and NumeroDeHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO") 