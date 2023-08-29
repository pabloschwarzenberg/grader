#Contestador de celular
llamada = input("Ingrese numero telefonico de 8 digitos: ")
hora = int(input("Ingrese hora de la llamada : "))

if hora > 12 and hora < 7 :
 print("CONTESTAR")
else:
    if hora < 14:
        if llamada[5:8] == "909":
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if hora > 17 and hora < 19:
            if llamada[0:3] == "877":
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if hora > 19:
                print("NO CONTESTAR")