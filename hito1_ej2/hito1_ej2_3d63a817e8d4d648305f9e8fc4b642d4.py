#Contestador de celular
# Entradas
num_tel = int(input("ingrese el número telefónico de 8 dígitos: "))
hora = int(input("ingrese la hora de su llamada: "))

#Genero la excepción para el número terminado en 909.
exc_1 = num_tel//1000
exc_1 *= 1000
exc_1 = num_tel - exc_1

#Evalúo que el número tenga 8 dígitos.
if num_tel//100000000 == 0:

#si la llamada ocurre entre 0 y 7 contesto.
    if 0 <= hora <= 7:
        print("CONTESTAR")
        
#si la llamada ocurre antes de las 14 NO CONTESTO, excepto term 909.       
    elif 7 < hora < 14:
        if exc_1 == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")

#durante la tarde contesto solo entre 17 y 19 menos empieza 877.
    elif 14 <= hora < 17:
        print("NO CONTESTAR")
    elif 17 <= hora <= 19:
        if 87700000 <= num_tel <= 87799999:
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
#despues de las 19 no contesto.
    elif 19 < hora <= 23:
        print("NO CONTESTAR")

#En el caso que no se cumplan, son datos erróneos.
    else:
        print("La hora ingresada no es válida.")
else:
    print("El número ingresado no es válido.")