#Zodiaco
dc=int(input())
mc=int(input())
if (mc==3 and dc>=21) or (mc==4 and dc<=20):
    print("aries")
elif mc==4 and dc>=21 or mc==5 and dc<=21:
    print("taurus")
elif mc==5 and dc>=22 or mc==6 and dc<=21:
    print("geminis")
elif mc==6 and dc>=22 or mc==7 and dc<=22:
    print("cancer")
elif mc==7 and dc>=23 or mc==8 and dc<=22:
    print("leo")
elif mc==8 and dc>=23 or mc==9 and dc<=23:
    print("virgo")
elif mc==9 and dc>=24 or mc==10 and dc<=23:
    print("libra")
elif mc==10 and dc>=24 or mc==11 and dc<=22:
    print("scorpio")
elif mc==11 and dc>=23 or mc==12 and dc<=21:
    print("sagitario")
elif mc==12 and dc>=22 or mc==1 and dc<=20:
    print("capricornio")
elif mc==1 and dc>=21 or mc==2 and dc<=19:
    print("aquarius")
elif mc==2 and dc>=20 or mc==3 and dc<=20:
    print("pisces")