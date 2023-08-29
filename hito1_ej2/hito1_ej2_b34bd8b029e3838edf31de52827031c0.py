#Contestador de celular
numero= int(input("Ingrese el número telefónico (8 dígitos): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))


if hora>= 0 and hora < 7:
    print("Resultado: CONTESTAR")
elif hora < 14 and numero % 100 == 9:
    print("Resultado: CONTESTAR")
elif hora>= 17 and hora< 19 and numero // 1000000 == 877:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")     