#Contestador de celular
num = input("numero ")
hora = int(input("Hora "))
numc = num[0:8]
numcc = num[5:8]
if num == numc:
    if (numcc == str("909")) and (hora <= 14) and (hora >= 8):
        print("Contestar")
    elif (hora >= 0) and (hora <= 7):
        print("Contestar emergencia")
    elif (hora >= 17) and (hora <=19) and (numcc == "877"):
        print("Contestar tarde")
    else:
        print("No contestar")
else:
    print("Numero incorrecto")