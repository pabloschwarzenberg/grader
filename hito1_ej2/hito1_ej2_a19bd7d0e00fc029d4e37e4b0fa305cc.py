#Contestador de celular
#nt= numero telefonivo
#h= hora

nt= str(input("por favor,ingrese un numero telefonico:"))
h= int(input("por favor, ingrese la hora de la llamada:"))
if h > 0 and h < 7:
    print("contestar")
if h > 19 and h <= 23:
    print("no contestar")
else:
    if h > 7 and h < 14 and str(nt[-3]) == "9" and str(nt[-2]) == "0" and str(nt[-1]) == "9":
        print("CONTESTAR")
    if h > 7 and h < 14 and str(nt[-3]) != "9" and str(nt[-2]) != "0" and str(nt[-1]) != "9":
        print("no contestar")
    if h > 17 and h < 19 and str(nt[0:1]) == "8" and str(nt[1:2]) == "7" and str(nt[2:3]) == "7":
        print("no contestar")
    if h > 17 and h < 19 and str(nt[0:1]) != "8" and str(nt[1:2]) != "7" and str(nt[2:3]) != "7":
        print("contestar")
