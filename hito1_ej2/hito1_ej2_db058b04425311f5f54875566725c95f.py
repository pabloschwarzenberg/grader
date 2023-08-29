#Contestador de celular
numero_de_telefono= int(input("ingrese numero telefonico: "))
hora_de_la_llamada= int(input("ingrese hora de llamada: "))
if len(str(numero_de_telefono)) >8:
    print("no existe")
else:
    if hora_de_la_llamada >0 and hora_de_la_llamada < 7: 
     print("CONTESTAR")
    elif hora_de_la_llamada <14 and str(numero_de_telefono)[4:] == "909":
     print("CONTESTAR")
    elif hora_de_la_llamada <14: 
     print("CONTESTAR")
    elif hora_de_la_llamada >17 and hora_de_la_llamada<19 and str(numero_de_telefono)[:3] != "877":
     print("CONTESTAR")
    elif hora_de_la_llamada >17 and hora_de_la_llamada<19: 
     print("NO CONTESTAR")
    if hora_de_la_llamada> 19:
     print("NO CONTESTAR")
