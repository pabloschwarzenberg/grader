#Contestador de celular

numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

if len(numero_telefonico) != 8 or not numero_telefonico.isdigit():
    print("Número telefónico inválido. Debe ser un número de 8 cifras.")
    exit()

if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == "909":
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    if numero_telefonico[:3] == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
