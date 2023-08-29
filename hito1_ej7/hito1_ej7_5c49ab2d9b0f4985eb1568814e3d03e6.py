#Zodiaco
dias=int(input("dias"))
mes=input("mes")
if (mes=="1" and dias>20) or (mes=="2" and dias<=19):
    print("aquarius")
elif(mes=="2" and dias>19) or (mes=="3" and dias<=21):
    print("pisces")
elif(mes=="3" and dias>21) or (mes=="4" and dias<=20):
    print("aries")
elif(mes=="4" and dias>20) or (mes=="5" and dias<=21):
    print("taurus")
elif(mes=="5" and dias>21) or (mes=="6" and dias<=21):
    print("geminis")
elif(mes=="6" and dias>21) or (mes=="7" and dias<=23):
    print("cancer")
elif(mes=="7" and dias>23) or (mes=="8" and dias<=23):
    print("leo")
elif(mes=="8" and dias>23) or (mes=="9" and dias<=23):
    print("virgo")
elif(mes=="9" and dias>23) or (mes=="10" and dias<=23):
    print("libra")
elif(mes=="10" and dias>23) or (mes=="11" and dias<=22):
    print("scorpio")
elif(mes=="11" and dias>22) or (mes=="12" and dias<=20):
    print("sagitario")
elif(mes=="12" and dias>20) or (mes=="1" and dias<=29):
    print("capricornio")
