#Contestador de celular

numero_t = input("Ingrese número de contacto (8 digitos): ")
hora = eval(input("Ingrese la hora de la llamada (0 a 23): "))

if ((0 < hora <= 7) and 8 == len(str(numero_t))):
    print("Resultado: CONTESTAR")

elif ((0 < hora <= 7) and 8 != len(str(numero_t))):
    print("Resultado: NO CONTESTAR, NUMERO NO ACEPTADO")

elif ((hora >= 19) and 8 == len(str(numero_t))):
    print("Resultado: NO CONTESTAR")

elif hora >= 19 and 8 != len(str(numero_t)):
    print("Resultado: NO CONTESTAR, NUMERO NO ACEPTADO")

else:
    if (hora <= 14) and 8 == len(str(numero_t)) and ((int(numero_t[5]) == 9) and (int(numero_t[6]) == 0) and (int(numero_t[7]) == 9)):
        print("Resultado: CONTESTAR")
    elif (hora <= 14) and 8 == len(str(numero_t)):
        print("Resultado: NO CONTESTAR")
    else:
        if (17 <= hora <= 19) and 8 == len(str(numero_t)) and ((int(numero_t[0]) == 8) and (int(numero_t[1]) == 7) and (int(numero_t[2]) == 7)):
            print("Resultado: NO CONTESTAR")
        elif ((17 <= hora <= 19) and 8 == len(str(numero_t))):
            print("Resultado: CONTESTAR")