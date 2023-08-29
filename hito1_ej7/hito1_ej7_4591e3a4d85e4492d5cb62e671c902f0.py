#Zodiaco
print("SIGNO DEL ZODIACO")
DIA= int(input("INGRESE SU DIA DE CUMPLEAÑOS: "))
MES= int(input("INGRESE SU MES DE CUMPLEÑAOS: "))
if DIA<=0 or DIA>31:
    print("ERROR")
    print("EL DIA DE CUMPLEAÑOS INGRESADO NO ES VALIDO")
    print("INGRESE UN DIA ENTRE 1 Y 31 POR FAVOR")
elif MES<=0 or MES>12:
    print("ERROR")
    print("EL MES DE CUMPLEAÑOS INGRESADO NO ES VALIDO")
    print("INGRESE UN MES ENTRE 1 Y 12 POR FAVOR")
elif MES==2 and (DIA==30 or DIA==31):
    print("ERROR")
    print("LA FECHA DE CUMPLEAÑOS INGRESADO NO ES VALIDA")
    print("INGRESE UNA FECHA EXISTENTE POR FAVOR")
else:
   if (MES==3 and DIA>=21)or(MES==4 and DIA<=19):
        print("ARIES")
   elif (MES==4 and DIA>=20)or(MES==5 and DIA<=20):
       print("TAURO")
   elif (MES==5 and DIA>=21)or(MES==6 and DIA<=21):
       print("GEMINIS")
   elif (MES==6 and DIA>=22)or(MES==7 and DIA<=22):
       print("CANCER")
   elif (MES==7 and DIA>=23)or(MES==8 and DIA<=23):
       print("LEO")
   elif (MES==8 and DIA>=24)or(MES==9 and DIA<=22):
       print("VIRGO")
   elif (MES==9 and DIA>=23)or(MES==10 and DIA<=23):
       print("LIBRA")
   elif (MES==10 and DIA>=24)or(MES==11 and DIA<=22):
       print("ESCORPIO")
   elif (MES==11 and DIA>=23)or(MES==12 and DIA<=22):
       print("SAGITARIO")
   elif (MES==12 and DIA>=23)or(MES==1 and DIA<=20):
       print("CAPRICORNIO")
   elif (MES==1 and DIA>=21)or(MES==2 and DIA<=18):
       print("ACUARIO")
   elif (MES==2 and DIA>=19)or(MES==3 and DIA<=20):
       print("PISCIS")      