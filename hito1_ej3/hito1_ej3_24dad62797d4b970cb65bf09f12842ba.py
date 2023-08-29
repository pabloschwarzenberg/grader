#Aprobación de créditos
Año = 2020
Ingreso = int(input("Digite sus ingresos \n"))
AñoDeNacimiento = int(input("Digite su año de naciemiento \n"))
NumHijos = int(input("Digite la cantidad de hijos \n"))
AñosBanco = int(input("Digite sus años en el banco \n"))

EstadoCivil = str(input("Ingrese si está soltero o casado con una S o una C \n"))
while (EstadoCivil != "S" and EstadoCivil != "C"):
    EstadoCivil = str(input("Ingrese si está soltero o casado con una S o una C \n"))

CampoCiudad = str(input("Ingrese si vive en zona urbana o rural con una U o una R \n"))
while (CampoCiudad != "R" and CampoCiudad != "U"):
    CampoCiudad = str(input("Ingrese si vive en zona urbana o rural con una U o una R  \n"))

    
Años = Año - AñoDeNacimiento

if (AñosBanco >= 11 and NumHijos >= 2):
    print ("APROBADO")

elif (EstadoCivil == "C" and NumHijos >= 4 and (Años >= 45 and Años <= 55)):
    print("APROBADO")

elif (Ingreso > 2500000 and EstadoCivil == "S" and CampoCiudad == "U"):
    print("APROBADO")

elif (Ingreso > 3500000 and AñosBanco > 5):
    print("APROBADO")

elif (CampoCiudad == "R" and EstadoCivil == "C" and NumHijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")