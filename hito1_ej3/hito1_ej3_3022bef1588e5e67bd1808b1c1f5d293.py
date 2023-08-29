#Aprobación de créditos
print("bienvenido, ingrese sus datos ")
ingreso = int(input("ingreso en pesos: "))
nacimiento = int(input("año de nacimiento: "))
Año_De_Nacimiento = (2021 - nacimiento)
hijos = int(input("numero de hijos: "))
pertenencia = int(input("años de pertenencia al banco: "))
estado = input("estado civil soltero o casado (S, C):  ")
locacion = input("¿vive en el campo o en la ciudad (R, U)?: ")

while True:
    
    if pertenencia > 10:
        if hijos > 1:
            print("APROBADO")
            break
    
    if estado == "C":
        if hijos > 3 and 44 < Año_De_Nacimiento < 56:
            print("APROBADO")
            break
        
    if ingreso > 2500000:
        if estado == "S" and locacion =="U":
            print("APROBADO")
            break
    
    if ingreso > 3500000:
        if pertenencia > 5:
            print("APROBADO")
            break
            
    if locacion == "R":
        if estado == "C" and hijos < 2:
            print("APROBADO")
            break
    else:
        print("RECHAZADO")
        break