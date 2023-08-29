#Aprobación de créditos
Ingreso = int(input("Registre su ingreso: $"))
AñoNacimiento = int(input("Registre el año de su nacimiento: "))
Hijos = int(input("Registre cantidad de hijos: "))
AñosPertenencia = int(input("Registre sus años de pertenencia en el banco: "))
EstadoCivil = input("S en caso de estar soltero, C en caso de estar casado: ")
Vive = input("U en caso de urbano, R en caso de rural: ")
Añoedad = AñoNacimiento >= 1965 and AñoNacimiento <= 1975

if AñosPertenencia > 10 and Hijos >= 2:
    print("APROBADO")
elif EstadoCivil == ("C" or "c") and Hijos > 3 and Añoedad:
    print("APROBADO")
elif Ingreso > 2500000 and EstadoCivil == ("S" or "s") and Vive == ("U" or "u"):
    print("APROBADO")
elif Ingreso > 3500000 and AñosPertenencia > 5:
    print("APROBADO")
elif Vive == ("R" or "r") and EstadoCivil == ("C" or "c") and Hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")
