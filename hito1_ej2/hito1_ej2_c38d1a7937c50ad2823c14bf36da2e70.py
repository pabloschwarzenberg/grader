#Contestador de celular
numero = str(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
ultnum = numero[5:8]
primnum = numero[0:3]
if (0 < hora < 7):
    print("Resultado: CONTESTAR")
elif (hora < 14) and ultnum == "909":
    print("Resultado: CONTESTAR")
elif (17 < hora < 19) and primnum != "877":
    print("Resultado: CONTESTAR")
elif (hora > 19):
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")      