#Aprobacion de Creditos
Ingreso = int(input("Ingreso en pesos: "))
Año_nacimiento = int(input("Ingres su año de nacimiento: "))
Hijos = int(input("Numero de hijos: "))
Años_banco = int(input("Ingrese sus años de pertenencia al banco: "))
Estado_civil = str(input("Ingrese su estado civil; S: soltero, C: casado: "))
Sector = str(input("Ingrese si vive en campo o ciudad; U: urbano, R: rural: "))

#Reglas para la aprobacion
if (Años_banco < 10, Hijos >= 2):
    print("APROBADO")
else:
    print("RECHAZADO")
if (Estado_civil == "C", Hijos > 3, 1976 < Año_nacimiento > 1966):
    print("APROBADO")
else:
    print("RECHAZADO")
if (Ingreso > 2500000, Estado_civil == "S", Sector == "U"):
        print("APROBADO")
else:
        print("RECHAZADO")
if (Ingreso > 3500000, Años_banco > 5):
        print("APROBADO")
else:
        print("RECHAZADO")
if (Sector == "R", Estado_civil == "C", Hijos < 2):
        print("APROBADO")
else:
        print("RECHAZADO")