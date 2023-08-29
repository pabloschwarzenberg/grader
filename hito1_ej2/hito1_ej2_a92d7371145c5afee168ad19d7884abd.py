#Contestador de celular
num = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada; "))

if hora >= 0 and hora <= 7:
    print("Resultado: CONTESTAR")
if hora > 7 and hora < 14 and num[5:] != "909":
    print("Resultado: NO CONTESTAR")
if 7 < hora < 14 and num[5:] == "909":
    print("Resultado: CONTESTAR")
if hora > 14 and hora <17:
    print("Resultado: NO CONTESTAR")
if hora >= 17 and hora <= 19 and num[:3] != "877":
    print("Resultado: CONTESTAR") 
if hora >= 17 and hora <= 19 and num[:3] == "877":
    print("Resultado: NO CONTESTAR") 
if hora > 19:
    print("Resultado: NO CONTESTAR")      