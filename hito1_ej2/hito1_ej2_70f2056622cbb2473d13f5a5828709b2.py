#Contestador de celular
num = str(int(input("Ingrese Numero de telefono: ")))
hora = int(input("Ingrese hora de la llamada: "))

print(num[:3])
if 0 < hora < 7:
    print("Contestar")

elif 7 < hora < 14:
    if num[-3:] == "909":
        print("Contestar")
    else:
        print("No contestar")

elif 17 < hora < 19:
    if num[:3] == "877":
        print("No contestar")
    else:
        print("Contestar")

elif hora > 19:
    print("No contestar")