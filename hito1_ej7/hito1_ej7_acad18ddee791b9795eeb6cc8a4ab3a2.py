#Zodiaco
a=int(input("Dia nacimiento:"))
b=int(input("Mes nacimiento:"))
if((b==3 and (a>=21))or(b==4 and a<=20)): print("aries")
else:
    if((b==4 and a>=21 )or(b==5 and a<=21)): print("tauro")
    else:
        if((b==5 and a>=22 )or(b==6 and a<= 21)):print("geminis")
        else:
            if((b==6 and a>= 22)or(b==7 and a<= 22)):print("cancer")
            else:
                if((b==7 and a>= 23)or(b==8 and a<=22 )):print("leo")
                else:
                    if((b==8 and a>=23 )or(b==9 and a<=23 )):print("virgo")
                    else:
                        if((b==9 and a>=24 )or(b==10 and a<=23 )):print("libra")
                        else:
                            if((b==10 and a>=24 )or(b==11 and a<=22 )):print("scorpio")
                            else:
                                if((b==11 and a>=23 )or(b==12 and a<=21 )):print("sagitario")
                                else:
                                    if((b==12 and a>=22 )or(b==1 and a<=20 )):print("capricornio")
                                    else:
                                        if((b==1 and a>=21 )or(b==2 and a<=19 )):print("aquarius")
                                        else:
                                            if((b==2 and a>=20 )or(b==3 and a<=20 )):print("pisces")



