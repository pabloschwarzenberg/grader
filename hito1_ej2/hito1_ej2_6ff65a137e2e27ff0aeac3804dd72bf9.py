#Contestador de celular
numero = input("ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))
if hora >= 0 and hora <= 7:
    Print("contestar")
elif hora < 14:
    if numero[-3:]=="909" :
         print("contestar")
    else:
         Print("no contestar")
elif hora >= 17 and hora <=19:
    if numero[:3]=="877":
        Print("no contestar")
    else:
        Print("contestar")
elif hora >= 19:
