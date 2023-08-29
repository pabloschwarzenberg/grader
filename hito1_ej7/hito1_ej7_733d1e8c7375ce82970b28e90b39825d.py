#Zodiaco
#entrada
dia=int(input("Día de su cumpleaños: "))
mes=int(input("Mes de su cumpleaños: "))
#fecha transformada a 1 solo numero
f=int(str(mes)+str(dia))

#ZODIACO
#Aries 21-03 / 20-04
if  (f>=321 and f<=331) or (f>=41 and f<=49) or(f>=410 and f<420):
    print("aries")    
#Tauro 20-04 / 21-05
elif    (f>=420 and f<=431) or (f>=51 and f<=59) or(f>=510 and f<521):
    print("tauro")
#Geminis 21-05 / 21-06
elif    (f>=521 and f<=531) or (f>=61 and f<=69) or(f>=610 and f<621):
    print("geminis")
#Cáncer 21-06 / 23-07
elif    (f>=621 and f<=631) or (f>=71 and f<=79) or(f>=710 and f<723):
    print("cancer")
#León 23-07 / 23-08
elif    (f>=723 and f<=731) or (f>=81 and f<=89) or(f>=810 and f<823):
    print("leon")
#Virgo 23-08 / 23-09
elif    (f>=823 and f<=831) or (f>=91 and f<=99) or(f>=910 and f<923):
    print("virgo")
#Libra 23-09 / 23-10
elif    (f>=923 and f<=931) or (f>=101 and f<=109) or(f>=1010 and f<1023):
    print("libra")
#Escorpión 23-10 / 22-11
elif    (f>=1023 and f<=1031) or (f>=111 and f<=119) or(f>=1110 and f<1122):
    print("escorpion")
#Sagitario 22-11 / 22-12
elif    (f>=1122 and f<=1131) or (f>=121 and f<=129) or(f>=1210 and f<1222):
    print("sagitario")
#Capricornio 22-12 / 20-01
elif    (f>=1222 and f<=1231) or (f>=11 and f<=19) or(f>=110 and f<120):
    print("capricornio")
#Acuario 20-01 / 19-02
elif    (f>=120 and f<=131) or (f>=21 and f<=29) or(f>=210 and f<219):
    print("acuario")
#Piscis 19-02 / 21-03
elif    (f>=219 and f<=229) or (f>=31 and f<=39) or(f>=310 and f<321):
    print("piscis")     