#Contestador de celular
phone_number = input("Ingrese numero de telefono: ")
time = int(input("Ingrese hora de llamada: "))

#Proceso

if time >= 0 and time <= 7:
    print("Contestar")

elif time > 7 and time <= 14 and phone_number[5:] == "909":
    print("Contestar")

elif time >= 17 and time <= 19 and phone_number[0:3] != "877":
    print("Contestar")
else: print("No contestar")
      