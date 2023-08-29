numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de llamada: "))
if len(str(numero))>8:
    print("el numero no existe")
else:
    if hora >0 and hora <7:
     print("contestar")
    elif hora <14 and str(numero)[4:] == "909":
     print("contestar")
    elif hora <14:
     print("contestar")
    elif hora >17 and hora <19 and str(numero)[:3] != "877":
     print("contestar")
    elif hora >17 and hora <19:
     print("no contestar")
    if hora >19:
     print("no contestar")