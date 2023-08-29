#Zodiaco
fecha = str(input("ingrese su fecha de cumpleaños: "))
#DIA
dia = [int(fecha[0]),int(fecha[1])]
mes = fecha[1]

if fecha[1] == " ":
    dia = int(fecha[0])
    mes= int(fecha[2])
    if len(fecha)== 3:
        mes= fecha[2]
        
    
else: dia == fecha[0]+fecha[1]


#MES
if fecha[1]== " ":
    if len(fecha)== 4:
        mes= fecha[2]+fecha[3]
if fecha[1]!=" ":
    if len(fecha)==4:
        mes= fecha[3]

if len(fecha)== 5:
    if fecha[0]+fecha[1]== 10:
        print("octubre")
#int(mes)#
        
if int(mes) == 3:
    if int(dia) < 20:
        print("aries")
if int(mes) == 4:
    if int(dia) < 21:
        print("aries")
if int(mes) == 4:
    if int(dia) > 20:
        print("tauro")
if int(mes) == 5:
    if int(dia) < 20:
        print("tauro")
if int(mes) == 5:
    if int(dia) > 20:
        print("géminis")
if int(mes) == 6:
    if int(dia) < 22:
        print("géminis")
if int(mes) == 6:
    if int(dia) > 21:
        print("cancer")
if int(mes) == 7:
    if int(dia) < 23:
        print("cancer")
if int(mes) == 7:
    if int(dia) > 22:
        print("leo")
if int(mes) == 8:
    if int(dia) < 24:
        print("leo")
if int(mes) == 8:
    if int(dia) > 23:
        print("virgo")
if int(mes) ==9:
    if int(dia) < 23:
        print("virgo")
if int(mes) == 9 :
    if int(dia) > 22:
        print("libra")
if int(mes) == 10 :
    if int(dia) < 24:
        print("libra")
if int(mes) == 10:
    if int(dia) > 23:
        print("escorpio")
if int(mes) == 11:
    if int(dia) < 23:
        print("escorpio")
if int(mes) == 11:
    if int(dia) > 22:
        print("sagitario")
if int(mes) == 12:
    if int(dia) < 23:
        print("sagitario")
if int(mes) == 12:
    if int(dia) > 22:
        print("capricornio")
if int(mes) == 1:
    if int(dia) < 21:
        print("capricornio")
if int(mes) == 1:
    if int(dia) > 20:
        print("acuario")
if int(mes) == 2:
    if int(dia) < 19:
        print("acuario")
if int(mes) == 2:
    if int(dia) > 18:
        print("piscis")
if int(mes) == 3:
    if int(dia) < 21:
        print("piscis")