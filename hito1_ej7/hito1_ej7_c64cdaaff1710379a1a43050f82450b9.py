#Zodiaco
d=int(input("dame tu dia de cumpleaños"))
m=int(input("dame tu mes de cumpleaños"))
if(m==1 and d>=21) or (m==2 and d<=19) :
    print("Aquarius")
elif(m==2 and d>=20) or (m==3 and d<=20):
    print("Pisces")
elif(m==3 and d>=21) or (m==4 and d<=20):
    print("Aries")
elif(m==4 and d>=21) or (m==5 and d<=21):
    print("Taurus")
elif(m==5 and d>=22) or (m==6 and d<=21):
    print("Gemini")
elif(m==6 and d>=22) or (m==7 and d<=22):
    print("Cancer")
elif(m==7 and d>=23) or (m==8 and d<=22):
    print("Leo")
elif(m==8 and d>=23) or (m==9 and d<=23):
    print("Virgo")
elif(m==9 and d>=24) or (m==10 and d<=23):
    print("Libra")
elif(m==10 and d>=24) or (m==11 and d<=22):
    print("Scorpio")
elif(m==11 and d>=23) or (m==12 and d<=21):
    print("Sagittarius")
elif (m==12 and d>=22) or (m==1 and d<=20):
    print("Capricorn")
 
