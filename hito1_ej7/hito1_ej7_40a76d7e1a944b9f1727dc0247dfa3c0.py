dia=int(input("escriba dia de cumpleaños: "))
mes=int(input("escriba mes de cumpleaños: "))

if( mes==3 and dia>=21 and dia<=31 ) or ( mes==4 and dia<=20 and dia>0 ):
    print("Aries")
elif( mes==4 and dia>=20 and dia<=30 ) or ( mes==5 and dia<=21 and dia>0 ):
    print("Tauro")
elif( mes==5 and dia>=21 and dia<=31 ) or ( mes==6 and dia<=21 and dia>0 ):
    print("geminis")
elif( mes==6 and dia>=21 and dia<=30 ) or ( mes==7 and dia<=23 and dia>0 ):
    print("cancer")
elif( mes==7 and dia>=23 and dia<=31 ) or ( mes==8 and dia<=23 and dia>0 ):
    print("leon")
elif( mes==8 and dia>=23 and dia<=31 ) or ( mes==9 and dia<=23 and dia>0 ):
    print("virgo")
elif( mes==9 and dia>=23 and dia<=30 ) or ( mes==10 and dia<=23 and dia>0 ):
    print("libra")
elif( mes==10 and dia>=23 and dia<=31 ) or ( mes==11 and dia<=22 and dia>0 ):
    print("escorpion")
elif( mes==11 and dia>=23 and dia<=30 ) or ( mes==12 and dia<=22 and dia>0 ):
    print("sagitario")
elif( mes==12 and dia>=22 and dia<=31 ) or ( mes==1 and dia<=20 and dia<0 ):
    print("capricornio")
elif( mes==1 and dia>=20 and dia<=31 ) or ( mes==2 and dia<=19 and dia<0 ):
    print("acuario")
elif( mes==2 and dia>=19 and dia<=28 ) or ( mes==3 and dia<=21 and dia>0 ):
    print("piscis")
else:
    print("no exciste")