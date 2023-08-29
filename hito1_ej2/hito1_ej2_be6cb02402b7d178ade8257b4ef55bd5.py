#Contestador de celular
#Entrada
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_de_llamada = int(input("Ingrese hora de la llamada: "))


if hora_de_llamada >= int(0) and hora_de_llamada <= int(7):
    print("CONTESTAR")
elif hora_de_llamada <= int(14) and numero_telefonico % 1000 == 909 :
    print("CONTESTAR")
elif hora_de_llamada <= int(14):
    print("NO CONTESTAR")
elif hora_de_llamada <= int(17) and hora_de_llamada >= int(19):
    print("CONTESTAR")
elif hora_de_llamada >= int(17) and hora_de_llamada <= int(19) and numero_telefonico//100000 == 877:
    print("NO CONTESTAR")
elif hora_de_llamada >= int(19):
    print("NO CONTESTAR")