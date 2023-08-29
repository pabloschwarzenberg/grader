#Contestador de celular
numero= input("Ingrese numero telefonico:")
hora= int(input("Ingrese hora de la llamada:"))

if hora>=0 and hora <=7:
    contestar = True
elif hora >7 and hora < 14 and numero[-3:]== "909":
    contestar= True
elif hora >7 and hora < 14 and not(numero[-3:]== "909"):
    contestar= False
elif hora >=14 and hora<=19 and numero[0:2]== "877":
    contestar= True
elif hora >=14 and hora<=19 and not(numero[0:2]== "877"):
    contestar= False
elif hora> 19 and hora <=23:
    contestar= False

if contestar:
    print ("CONTESTAR")
else:
    print ("NO CONTESTAR")