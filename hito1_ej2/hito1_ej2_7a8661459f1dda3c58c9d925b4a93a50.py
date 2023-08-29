#contestador de llamadas

numero_telefonico = str(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de llamada: "))

i = hora_llamada

if i >= 0 and i <= 7:
    print("Contestar")

if i <= 14 and i > 7:
    if numero_telefonico[-3:] == "909":
        print("Contestar")
    else:
        print("No contestar")

if i >= 17 and i <= 19:
    if numero_telefonico[0:3] == "877":
        print("No contestar")
    else:
        print("Contestar")

if i > 19:
    print("No contestar")
      