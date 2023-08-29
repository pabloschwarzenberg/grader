dia=int(input())
mes=int(input())
if mes==1:
    if dia<=20:
        print("Capricornio")
    else:
         print("Acuario")
elif mes==2:
    if dia<=19:
        print("Acuario")
    else:
        print("Piscis")
elif mes==3:
    if dia<=20:
        print("Piscis")
    else:
        print("Aries")
elif mes==4:
    if dia<=20:
        print("Aries")
    else:
        print("Tauro")
elif mes==5:
    if dia<=21:
        print("Tauro")
    else:
        print("Gemeni")
elif mes==6:
    if dia<=21:
        print("Gemini")
    else:
        print("Cancer")
elif mes==7:
    if dia<=22:
        print("Cancer")
    else:
        print("Leo")
elif mes==8:
    if dia<=22:
        print("Leo")
    else:
        print("Virgo")
elif mes==9:
    if dia<=23:
        print("Virgo")
    else:
        print("Libra")
elif mes==10:
    if dia<=23:
        print("Libra")
    else:
        print("Scorpio")
elif mes==11:
    if dia<=23:
        print("Scorpio")
    else:
        print("Sagitario")
else:
    if dia<=21:
        print("Sagitario")
    else:
        print("Capricornio")

