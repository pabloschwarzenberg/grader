#Contestador de celular
nro_telefonico = int(input())
hora_de_llamada = int(input())
if hora_de_llamada >= 0 and hora_de_llamada <= 7:
    print("CONTESTAR")
elif hora_de_llamada > 7 and hora_de_llamada <= 14:
    if nro_telefonico%10**3 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora_de_llamada >= 17 and hora_de_llamada <= 19:
    if str(nro_telefonico)[:3] == 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora_de_llamada <= 19 and hora_de_llamada <=23:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")