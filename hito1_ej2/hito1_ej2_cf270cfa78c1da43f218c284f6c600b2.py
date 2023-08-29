numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (formato 24 horas): "))
if 0 <= hora_llamada < 7:
    respuesta = "CONTESTAR"
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    respuesta = "CONTESTAR"
elif 17 <= hora_llamada < 19 and numero_telefonico // 1000000 == 877:
    respuesta = "CONTESTAR"
else:
    respuesta = "NO CONTESTAR"
print("Resultado:", respuesta)
