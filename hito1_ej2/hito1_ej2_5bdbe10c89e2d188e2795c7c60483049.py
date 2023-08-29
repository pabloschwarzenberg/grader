#Contestador de celular
numero= int(input("ingrese numero telefonico: "))
hora= int(input("ingrese hora de llamada: "))
if len(str(numero)) >8:
    print("no existe")
else:
    if hora >0 and hora < 7: 
     print("CONTESTAR")
    elif hora <14 and str(numero)[4:] == "909":
     print("CONTESTAR")
    elif hora <14: 
     print("CONTESTAR")
    elif hora >17 and hora<19 and str(numero)[:3] != "877":
     print("CONTESTAR")
    elif hora >17 and hora<19: 
     print("NO CONTESTAR")
    if hora> 19:
     print("NO CONTESTAR")