def contestar_llamada(hora, numero):
    condiciones = [
        hora >= 0 and hora <= 7,
        hora < 14 and numero % 100 == 9,
        hora >= 17 and hora <= 19 and numero // 10000000 == 877
    ]
    if any(condiciones):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_llamada(hora_llamada, numero_telefonico)
print("Resultado:", resultado)
