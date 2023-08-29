#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
if(len(str(numero)) == 8):
    if(hora >= 0 and hora <= 23):
        if(hora >= 0 and hora <= 7):
            print("CONTESTAR")
        if(hora < 14 and str(numero)[5:8] != "909"):
            print("NO CONTESTAR")
        if(hora < 14 and str(numero)[5:8] == "909"):
            print("CONTESTAR")
        if(hora >= 17 and hora <= 19 and str(numero)[0:3] != "877"):
            print("CONTESTAR")
        if(hora >= 17 and hora <= 19 and str(numero)[0:3] == "877"):
            print("NO CONTESTAR")
        if(hora > 19):
            print("NO CONTESTAR")