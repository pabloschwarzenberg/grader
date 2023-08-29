#Contestador de celular
#Contestador de celular
Nro = input("Ingrese número de celular: ")
Hra = int(input("Ingrese hora de la llamada"))
contestado = False
if Hra < 8:
    print ("CONTESTAR")
    contestado = True
if Hra < 14:
    if contestado == False:
        if "909" in Nro:
            print("CONTESTAR")
            contestado = True
if Hra > 16 and Hra < 20:
    if contestado == False:
        if "877" in Nro:
            print("NO CONTESTAR")
            contestado == True
        else: print("CONTESTAR")
        contestado == True
elif contestado == False:
    print("NO CONTESTAR")