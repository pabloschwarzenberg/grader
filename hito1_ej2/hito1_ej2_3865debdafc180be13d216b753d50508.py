#Contestador de celular
num = str(input("ingrese el numero telefonico: "))
hora = int(input("ingrese la hora de llamada: "))

PD = num[0:3]
UD = num[5:8]
if 0 <= hora <=7:
    print("contestar")
elif 7 < hora <= 14:
        if UD == "909":
            print("contestar")
        else:
            print("no contestar")
elif 17 <= hora <= 19:
        if PD == "877":
            print("no contestar")
        else:
            print("contestar")
else:
        print("no contestar")    