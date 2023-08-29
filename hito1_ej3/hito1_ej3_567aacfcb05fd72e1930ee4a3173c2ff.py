#Aprobación de créditos

Ingreso = int(input("Ingresar su ingreso en pesos: "))

AñoNacimiento = int(input("Ingresar año de nacimiento: "))

Hijos = int(input("Ingresar cantidad de hijos: "))

AñosBanco = int(input("Ingresar cantidad de años en el banco: "))

EstadoCivil = input("Ingresar su estado civil (S para Soltero y C para Casado): ")

Ubicación = input("¿Vive en zona rural o urbana? Seleccionar R para rural y U para Urbano: ")

Edad = 2022 - AñoNacimiento

while (Ingreso < 0):
    print("No se puede tener un ingreso negativo")
    Ingreso = int(input("Ingresar su ingreso en pesos: "))

while (AñoNacimiento < 0):
    print("No se puede tener un año de nacimiento negativo")
    AñoNacimiento = int(input("Ingresar año de nacimiento: "))

while (Hijos < 0):
    print("No se puede tener hijos negativos")
    Hijos = int(input("Ingresar cantidad de hijos: "))

while (AñosBanco < 0):
    print("No se pueden tener años negativos")
    AñosBanco = int(input("Ingresar cantidad de años en el banco: "))

if (AñosBanco > 10 and Hijos >= 2):
    print("APROBADO")

elif (str(EstadoCivil) == "C" and Hijos > 3 and 45 <= Edad <= 55):
    print("APROBADO")

elif (Ingreso > 2500000 and str(EstadoCivil) == "S" and str(Ubicación) == "U"):
    print("APROBADO")

elif (Ingreso > 3500000 and AñosBanco > 5):
    print("APROBADO")

elif (str(Ubicación) == "R" and str(EstadoCivil) == "C" and Hijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")