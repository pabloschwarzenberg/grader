numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

#hora
if hora_llamada >= 0 and hora_llamada < 7:
    print("Resultado: CONTESTAR")

#hora
elif hora_llamada < 14:
    # Verificar si el número termina en 909
    if numero_telefonico % 1000 == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")

#hora
elif hora_llamada >= 17 and hora_llamada < 19:
    
    if numero_telefonico // 1000000 == 877:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")


else:
    print("Resultado: NO CONTESTAR")