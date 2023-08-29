#Aprobación de créditos
print("Postulacion de creditos de consumo")
Ingreso = int(input("Sus ingresos: "))
Año_nacimiento = int(input("Año de nacimiento: "))
Hijos = int(input("Numero de hijos que tiene actualmente: "))
Año_pertenencia = int(input("Años de pertenencia en nuestro banco: "))
Estado_Civil = str(input("Estado Civil, si esta soltero escriba una S, si esta casado una C: "))
Campo_Ciudad = str(input("¿Reside en Campo o Ciudad? Si es en ciudad escriba U, de ser de campo, escriba R: "))
if (Año_pertenencia >= 10) and (Hijos >= 2):
    print("APROBADO")
else:
    if (Estado_Civil == "C") and (Hijos >= 3) and (Año_nacimiento <= 1976) and (Año_nacimiento >= 1966):
        print("APROBADO")
    else:
        if (Ingreso > 2500000) and (Estado_Civil == "S") and (Campo_Ciudad == "U"):
            print("APROBADO")
        else:
            if (Ingreso > 3500000) and (Año_pertenencia > 5):
                print("APROBADO")
            else:
                if (Campo_Ciudad == "R") and (Estado_Civil == "C") and (Hijos < 2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")