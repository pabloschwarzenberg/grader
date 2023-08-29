#Contestador de celular
numerotel = input("Numero telefonico: ")
hora = eval(input("Hora: "))

if 0 <= hora <= 7:
    contestar = True
elif hora < 14 and numerotel[5:8] == "909":
    contestar = True
elif hora < 14 and numerotel[5:8] != "909":
    contestar = False
elif 17 < hora < 19 and numerotel[0:3] == "877":
    contestar = False
elif 17 < hora < 19 and numerotel[0:3] != "877":
    contestar = True
elif 19 < hora < 23:
    contestar = False

if contestar == True:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")