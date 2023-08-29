#Aprobación de créditos
Ingresos = int(input("Ingreso en pesos "))
FechaNacimiento = int(input("Año de nacimiento "))
NumeroHijos = int(input("Numero de hijos "))
TiempoPertenencia = int(input("Años de pertenencia al banco "))
EstadoCivil = input("Estado civil ")
CampoCiudad = input("Vive en zona Rural/Urbana ")
Edad = 2022 - FechaNacimiento

if TiempoPertenencia >= 10 and NumeroHijos >= 2:
    print("APROBADO")
elif EstadoCivil == "C" and NumeroHijos > 3:
    if Edad > 45 and Edad < 55:
        print("APROBADO")
elif Ingresos > 2500000 and EstadoCivil == "S":
    if CampoCiudad == "U":
        print("APROBADO")
        
elif Ingresos > 3500000 and TiempoPertenencia > 5:
    print("APROBADO")
elif CampoCiudad == "R" and EstadoCivil == "C":
    if NumeroHijos < 2:
        print("APROBADO")
else:
    print("RECHAZADO")
    
    