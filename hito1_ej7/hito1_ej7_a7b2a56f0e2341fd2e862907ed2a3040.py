#Zodiaco
a=int(input("día:"))
b=int(input("mes:"))

if((b==3) and (31>=a>=21)) or ((b==4) and (20>=a>=1)):
    print("Aries")
elif((b==4) and (30>=a>=21)) or ((b==5) and (21>=a>=1)):
    print("Taurus")
elif((b==5) and (31>=a>=22)) or ((b==6) and (21>=a>=1)):
    print("Gemini")
elif((b==6) and (30>=a>=22)) or ((b==7) and (22>=a>=1)):
    print("Cancer")
elif((b==7) and (31>=a>=23)) or ((b==8) and (22>=a>=1)):
    print("Leo")
elif((b==8) and (31>=a>=23)) or ((b==9) and (23>=a>=1)):
    print("Virgo")
elif((b==9) and (30>=a>=24)) or ((b==10) and (23>=a>=1)):
    print("Libra")
elif((b==10) and (31>=a>=22)) or ((b==11) and (22>=a>=1)):
    print("Scorpio")
elif((b==11) and (30>=a>=23)) or ((b==12) and (21>=a>=1)):
    print("Sagittarius")
elif((b==12) and (31>=a>=22)) or ((b==1) and (20>=a>=1)):
    print("Capricorn")
elif((b==1) and (31>=a>=21)) or ((b==2) and (19>=a>=1)):
    print("Aquarius")
elif((b==2) and (28>=a>=19)) or ((b==3) and (20>=a>=1)):
    print("Pisces")
else:
    print("Ophiuchus")     