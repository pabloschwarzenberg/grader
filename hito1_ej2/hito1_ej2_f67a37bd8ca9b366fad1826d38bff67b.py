#Contestador de celular
numero=str(input("Numero telefóno: "))
hora=int(input("Hora de la llamada: "))
nF=(numero[7],numero[6],numero[5])
nI=(numero[0],numero[1],numero[2])

if hora>0 and hora<7:
    print("contestar")
if hora>7 and hora<14:
    if nF == ('9', '0', '9'):
        print("contestar")
    else:
        print("no contestar")
if hora>14 and hora<17:
    print("no contestar")
if hora>17 and hora<19:
    if nI == ('8', '7', '7'):
        print("no contestar")
    else:
        print("contestar")
if hora>19:
    print("no contestar")
