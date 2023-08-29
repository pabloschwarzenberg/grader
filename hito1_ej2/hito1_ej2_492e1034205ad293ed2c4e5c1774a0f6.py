def contestador_automatico():
    numero = int(input("Ingrese número telefónico: "))
    hora = int(input("Ingrese hora de la llamada: "))

    if hora >= 0 and hora <= 7:
        print("CONTESTAR")
    elif hora < 14 and numero % 100 == 9:
        print("CONTESTAR")
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

contestador_automatico()