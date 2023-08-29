llamada = int(input("Digite su numero telefonico: "))
hora = int(input("horario planeado para llamar: "))
sos= llamada%1000
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
if hora > 7 and hora <= 14 and sos == 909:
    print("CONTESTAR")
if hora > 7 and hora <= 14 and sos != 909:
    print("NO CONTESTAR")
if hora > 14 and hora <17:
    print("NO CONTESTAR")
if hora >= 17 and hora < 19 and llamada > 87699999 and llamada < 87800000:
    print("NO CONTESTAR")
if hora >= 17 and hora <= 19 and llamada < 87699999 and llamada > 87800000:
    print("CONTESTAR")
if hora > 19:
    print("NO CONTESTAR")