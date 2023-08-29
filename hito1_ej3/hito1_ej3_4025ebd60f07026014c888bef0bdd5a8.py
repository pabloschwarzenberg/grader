Ingreso = int(input("ingresar valor: "))
AñoDeNacimiento = int(input("ingresar año de nacimiento: "))
NumeroDeHijos = int(input("ingresar numero de hijos: "))
AñosDePertenenciaAlBanco = int(input("ingresar años de pertenencia al banco: "))
EstadoCivil = input("ingresar estado civil S o C: ")
DondeVive = input("ingresar U o R: ")
x = 10

if x > 10 and x >= NumeroDeHijos:
    print ("APROBADO")
elif x < 10 and x <= NumeroDeHijos:
    print ("RECHAZADO")
elif EstadoCivil == "C" and NumeroDeHijos > 3 and 45 <= AñoDeNacimiento - 2020 >= 55:
    print("APROBADO")
elif EstadoCivil == "S" and NumeroDeHijos < 3 and 45 <= AñoDeNacimiento - 2020 >= 55:
    print("RECHAZADO")
elif Ingreso > 2500000 and EstadoCivil == "S" and DondeVive == "U":
    print("APROBADO")
elif Ingreso < 2500000 and EstadoCivil == "C" and DondeVive == "R":
    print("RECHAZADO")
elif Ingreso > 3500000 and AñosDePertenenciaAlBanco > 5:
    print("APROBADO")
elif Ingreso < 3500000 and AñosDePertenenciaAlBanco < 5:
    print("RECHAZADO")
elif DondeVive == "R" and EstadoCivil == "C" and NumeroDeHijos < 2:
    print("APROBADO")
elif DondeVive == "U" and EstadoCivil == "S" and NumeroDeHijos > 2:
    print("RECHAZADO")
resultado=(str(Ingreso) + "," + str(AñoDeNacimiento - 2020) + "," + str(NumeroDeHijos) + "," + str(AñosDePertenenciaAlBanco) + "," + str(EstadoCivil) + "," + str(DondeVive))
print(resultado, "APROBADO")