#Aprobación de créditos

#Datos del usuario
while True:
    L = int(input("Ingrese el monto de sus ingresos en pesos:  "))
    AN = int(input("Ingrese su año de nacimiento:  "))
    NH = int(input("Ingrese el numero de hijos:  "))
    APB = int(input("Ingrese sus años de pertenencia al banco:  "))
    EC = input("Ingrese su estado civil (S: Soltero ; C: Casado):  ")
    TV = input("Ingrese si viven en campo o ciudad (U: Urbano ; R: Rural):  ")
    if L > 0 and AN >= 1900 and AN <= 2003 and NH >= 0 and APB >= 0 and (EC == "C" or EC == "S") and (TV == "U" or TV == "R"):    
        if APB >= 10 and NH >= 2:
            respuesta = "APROBADO"
        elif EC == "C" and AN <=1976 and AN >= 1966:
            respuesta = "APROBADO"
        elif L > 2500000 and EC == "S" and TV == "U":
            respuesta = "APROBADO"
        elif L > 3500000 and APV > 5:
            respuesta = "APROBADO"
        elif TV == "R" and EC == "C" and NH < 2:
            respuesta = "APROBADO"
        else:
            respuesta = "RECHAZADO"
        print(respuesta)
        break
    else:
        print("La respuesta ingresada en alguno de los requerimientos es incorrecta. Porfavor intentelo de nuevo.")