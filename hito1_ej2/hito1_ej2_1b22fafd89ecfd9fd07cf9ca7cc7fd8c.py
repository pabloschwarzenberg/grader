#Contestador de celular
numero = int(input("ingrese el numero telefonico: "))
hora = int(input("ingrese la hora de llamada: "))
if len(str(numero))>8:
    print("el numero que esta llamando no existe")
else:
    if hora >0 and hora <7:
     print("contestarle")
    elif hora <14 and str(numero)[4:] == "909":
     print("contestarle")
    elif hora <14:
     print("contestarle")
    elif hora >17 and hora <19 and str(numero)[:3] != "877":
     print("contestarle")
    elif hora >17 and hora <19:
     print("no contestarle")
    if hora >19:
     print("no contestarle")      