numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada < 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    if numero_telefonico % 1000 == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 18:
    if numero_telefonico // 10000000 == 877:
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
