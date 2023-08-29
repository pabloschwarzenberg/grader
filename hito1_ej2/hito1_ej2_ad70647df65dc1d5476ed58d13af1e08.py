#Contestador de celular
num_telefono = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada < 7:
    print("CONTESTAR")
elif hora_llamada >= 7 and hora_llamada < 14:
    if num_telefono % 100 == 9:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 18:
    if num_telefono // 1000000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
