telefono = int(input("Ingrese el número telefónico: "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))


if hora >= 0 and hora <= 7:
    
    print("Resultado: CONTESTAR")
elif hora < 14 and telefono % 1000 == 909:
    
    print("Resultado: CONTESTAR")
elif hora >= 17 and hora < 19 and telefono // 1000000 != 877:
    
    print("Resultado: NO CONTESTAR")
else:
    
    print("Resultado: NO CONTESTAR")