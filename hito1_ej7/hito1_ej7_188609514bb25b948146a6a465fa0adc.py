#Zodiaco
dia=int(input("dia: "))
mes=int(input("mes: "))
if mes==1 :
    m=0
if mes==2 :
    m=31   
if mes==3 :
    m=59
if mes==4 :
    m=90
if mes==5 :
    m=121
if mes==6 :
    m=151
if mes==7 :
    m=182
if mes==8 :
    m=212
if mes==9 :
    m=243
if mes==10 :
    m=273
if mes==11 :
    m=304
if mes==12 :
    m=334
    
n=(m + dia)
if n>=21 and n<51 :
    print("acuario")
if n>=51 and n<79 :
    print("piscis")
if n>=79 and n<111 :
    print("aries")
if n>=111 and n<142 :
    print("tauro")
if n>=142 and n<173 :
    print("gemeni")
if n>=173 and n<203 :
    print("cancer")
if n>=203 and n<234 :
    print("leo")
if n>=234 and n<266 :
    print("virgo")
if n>=266 and n<297 :
    print("libra")
if n>=297 and n<327 :
    print("escorpio")
if n>=327 and n<357 :
    print("sagitario")
if n>=357 or n<21 :
    print("capricornio")
