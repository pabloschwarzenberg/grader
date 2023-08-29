from datetime import date


ingreso = 0
nacimiento = 0
hijos = 0
añosPertenencia = 0
estadoCivil = ""
lugar = ""
bandera = True

while(bandera):
    ingreso = float(input("Ingrese su ingreso en pesos\n"))
    nacimiento = int(input("Ingrese su año de nacimiento\n"))
    hijos = int(input("Ingrese la cantidad de hijos que tiene actualmente\n"))
    añosPertenencia = int(input("Ingrese los años de pertenencia al banco\n"))
    estadoCivil = input("Ingrese su estado civil S = soltero, C = casado\n")
    lugar = input("Ingrese si vive en campo o en ciudad U = urbano, R = rural\n")
    
    añoNacimiento = 2021 - nacimiento
    if(estadoCivil != "S" and estadoCivil != "C"):
        print("Ingresó mal el estado civil, favor de ingresarlo correctamente")
        break
    elif(lugar != "U" and lugar != "R"):
        print("Ingresó mal el lugar donde vive, favor de ingresarlo correctamente")
        break
    elif(añosPertenencia > 10 and hijos >= 2):
        print("APROBADO")
    elif(estadoCivil == "C" and hijos > 3 and añoNacimiento >= 45 and añoNacimiento <= 55):
        print("APROBADO")
    elif(ingreso > 2500000 and estadoCivil == "S" and lugar == "U"):
        print("APROBADO")
    elif(ingreso > 3500000 and añosPertenencia > 5):
        print("APROBADO")
    elif(lugar == "R" and estadoCivil == "C" and hijos < 2):
        print("APROBADO")
    else:
        print("RECHAZADO")