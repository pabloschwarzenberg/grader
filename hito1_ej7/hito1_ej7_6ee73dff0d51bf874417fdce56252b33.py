#Zodiaco
dia=int(input("dia "))
mes=int(input("mes "))

if(mes==3):
 if(dia>=21): 
  print("Aries")
 if(dia<=20):
  print("Pisces")

if(mes==4):
 if(dia>=21):
     print("Taurus")
 else:
     print("Aries")

if(mes==5):
    if(dia>=22):
        print("Gemini")
    else:
        print("Taurus")

if(mes==6):
    if(dia>=22):
        print("Cancer")
    else:
        print("Gemini")

if(mes==7):
    if(dia>=23):
        print("Leo")
    else:
        print("Cancer")

if(mes==8):
    if(dia>=23):
        print("Virgo")
    else:
        print("Leo")

if(mes==9):
    if(dia>=24):
        print("Libra")
    else:
        print("Virgo")

if(mes==10):
    if(dia>=24):
        print("Scorpio")
    else:
        print("Libra")

if(mes==11):
    if(dia>=23):
        print("Sagittarius")
    else:
        print("Scorpio")

if(mes==12):
    if(dia>=22):
        print("Capricorn")
    else:
        print("Sagittarius")

if(mes==1):
    if(dia>=21):
        print("Aquarius")
    else:
        print("Capricorn")

if(mes==2):
    if(dia>=20):
        print("Pisces")
    else:
        print("Aquarius")
