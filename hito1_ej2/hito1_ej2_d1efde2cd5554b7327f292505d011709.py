NT = int(input("ingrese numero telefonico "))
H = int(input("ingrese hora de la llamada "))
umil = NT / 1000
tmp = NT % 1000
centenas = int(tmp / 100)
tmp = tmp % 100
decenas = int(tmp / 10)
unidades = int(tmp % 10)
u8 = int(NT / 10000000)
tmp2 = int(NT % 10000000)
u7 = int(tmp2 / 1000000)
tmp2 = int(tmp2 % 1000000)
u6 = int(tmp2 / 100000)
tmp2 = int(tmp2 % 100000)

numero_incorrecto=True
while numero_incorrecto==True:
    if NT<100000000 and NT>9999999:
        numero_incorrecto=False
    else:
        print("numero incorrecto")
if numero_incorrecto==False:
    if 0<H<7:
        print("Contestar")
    elif 7<=H<14 and centenas==9 and decenas==0 and unidades==9:
        print("Contestar")
    elif 7<=H<14:
              print("No Contestar")
    elif 14<=H<17:
              print("No Contestar")
    elif 17<=H<=19 and u8==8 and u7==7 and u6==7:
              print("No Contestar")
    elif 17<=H<=19:
              print("Contestar")
    elif H>19:
              print("No Contestar")

