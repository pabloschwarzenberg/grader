telefono = int(input("Ingrese su numero de telefono, recuerde que debe tener 8 digitos: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

if len(str(telefono)) != 8:
    print("Número telefónico inválido. Debe tener 8 dígitos.")
else:
    contestar = False
    if hora >= 0 and hora <= 7:
        contestar = True
    elif hora < 14 and str(telefono).endswith('909'):
        contestar = True
    elif hora >= 17 and hora <= 19 and str(telefono).startswith('877'):
        contestar = False
    if contestar:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
