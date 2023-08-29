numero = int(input("Ingrese el número de teléfono de 8 digitos: "))
hora_llamada = int(input("Ingrese la hora de la llamada(entre 0 y 23 horas): "))
if 0 < hora_llamada < 7:
    print("CONTESTAR")
elif 7 < hora_llamada < 14:
    if str(numero)[-3:] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 < hora_llamada < 19:
    if str(numero)[:3] == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif 19 < hora_llamada:
    print("NO CONTESTAR")