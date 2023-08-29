ingreso = int(input("Indique su ingreso en pesos:"))
año_nacimiento = int(input("Indique su año de nacimiento:"))
n_hijos = int(input("Indique la cantidad de hijos que tiene:"))
años_en_banco = int(input("Indique la cantidad de años que lleva en el banco:"))
estado_civil = input("Ingrese una C si está casado o una S si está soltero:")
ubicacion = input("Ingrese una U si vive en zona urbana o una R si vive en zona rural:")
edad = 2020 - año_nacimiento
if((años_en_banco >= 10 and n_hijos >= 2)):
    print("APROBADO")
if(estado_civil == "C" and n_hijos >3 and (edad >= 45 or edad <= 55)):
    print("APROBADO")
if(ingreso > 2500000 and estado_civil == "S" and ubicacion == "U"):
    print("APROBADO")
if(ingreso > 3500000 and años_en_banco > 5):
    print("APROBADO")
if(ubicacion == "R" and estado_civil == "C" and n_hijos < 2):
    print("APROBADO")
print("RECHAZADO")
