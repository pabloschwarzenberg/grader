numero = int(input("Ingresar numero de telefono:"))
ultimos_tres = numero % 1000
primeros_tres = numero // 100000
hora = int(input("Ingrese la hora:"))

if hora > 0 and hora < 7:
    print("Resultado: CONTESTAR")
elif hora > 7 and hora < 14:
    if ultimos_tres == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora > 17 and hora < 19:
    if primeros_tres == 877:
        print("Resultado: NO CONTESTAR")
    print("Resultado: CONTESTAR")
elif hora > 19:
    print("Resultado: NO CONTESTAR")