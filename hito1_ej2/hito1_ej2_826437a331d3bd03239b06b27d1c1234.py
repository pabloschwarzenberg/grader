#Contestador de celular
respuestas = ["NO CONTESTAR", "CONTESTAR"]
numero = int(input("Ingrese numero telefonico: "))
llamada = int(input("Ingrese hora de la llamada: "))
if llamada >= 19 or 14 <= llamada <= 17:
    print(respuestas[0])
elif 0 <= llamada <= 7:
    print(respuestas[1])
elif 7 <= llamada <= 14:
    if (numero % 1000) == 909:
        print(respuestas[1])
    else:
        print(respuestas[0])
elif 17 <= llamada <= 19:
    if (numero // 100000) != 877:
        print(respuestas[1])
    else:
        print(respuestas[0])