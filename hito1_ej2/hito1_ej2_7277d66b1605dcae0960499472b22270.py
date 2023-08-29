#Contestador de celular
numero = int(input ("Ingre el número telefónico (SOLO 8 DIGITOS): "))
HORA = int(input("Ingrese la hora de la llamada (0.23): "))

if HORA >= 0 and HORA <= 7:
    print("CONTESTAR LLAMADA")
elif HORA < 14:
    if numero % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif HORA >= 17 and HORA <= 19:
    if numero // 100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")  
else:
    print("NO CONTESTAR")      