#Contestador de celular
numtel= str(input("--> ingrese numero telefonico -->: "))
hora= int(input("--> ingrese hora de la llamada --> : "))

primdig = numtel[0:3]
ultidig = numtel[5:8]

if 0 <= hora <= 7:
    print("Resultado: CONTESTAR")

elif 7< hora <= 14:
    if ultidig == "909":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")

elif 17 <= hora <= 19:
    if primdig == "877":
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")

else:
    print("Resultado: NO CONTESTAR")