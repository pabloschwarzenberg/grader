#Contestador de celular
numero_telefono = 0
hora = 0
numero_telefono = input("Ingrese numero de Telefono; ")
hora = int(input("Ingrese la hora de llamada: "))
ultimos_numeros = numero_telefono[-3:]
primeros_numeros = numero_telefono [:3]
if hora > 0 and hora <= 7:
    print("contestar")
elif hora > 7 and hora < 14:
    if ultimos_numeros == "909":
        print("contestar")
    else:
        print("no contestar")
elif hora > 17 and hora < 19:
    if primeros_numeros == "877":
        print("no contestar")
    else:
        print("contestar")
elif hora > 19:
    print("no contestar")