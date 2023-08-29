#Aprobación de créditos
Ingresos = int(input("Ingresar ingresos: "))
Nacimiento = input("Ingresar año de nacimiento: ")
NumeroHijos = input("Ingresar numero de hijos: ")
AñosBanco = int(input("Ingresar cuantos años lleva en el banco: "))
EstadoCivil = input("Estado civil, soltero(S) o casado(C): ")
DondeVive = input("Ingresar donde vive, campo(R) o ciudad(U)")

Edad = (2020-int(Nacimiento))

EC = EstadoCivil.upper()
DV = DondeVive.upper()

if((int(AñosBanco) > 10) and int(NumeroHijos) >= 2):
    print("APROBADO")
elif((EC == "C") and (int(NumeroHijos) > 3) and (int(Edad) > 45) and (int(Edad) < 55)):
    print("APROBADO")
elif((Ingresos > 2500000) and (EC == "S") and (DV == "U")):
    print("APROBADO")
elif((Ingresos > 3500000) and (AñosBanco > 5)):
    print("APROBADO")
elif((DV == "R") and (EC == "C") and (int(NumeroHijos) < 2)):
    print(("APROBADO"))
else:
    print("RECHAZADO")