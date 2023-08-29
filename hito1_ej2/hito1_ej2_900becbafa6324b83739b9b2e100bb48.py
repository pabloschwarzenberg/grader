#Contestador de celular
telefonico = int(input("Ingrese el número telefónico de 8 dígitos: "))
llamada = int(input("Ingrese la hora de la llamada entre las horas 0hr y 23hr: "))

contestar = False

if llamada >= 0 and llamada < 7:
    contestar = True
elif llamada < 14 and telefonico % 100 == 9:
    contestar = True
elif llamada >= 17 and llamada < 19 and telefonico // 1000000 == 877:
    contestar = True

if contestar:
    resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"

print("Resultado:", resultado)      