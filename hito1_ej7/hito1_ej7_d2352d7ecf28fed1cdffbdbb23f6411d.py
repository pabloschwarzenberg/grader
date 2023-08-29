#Zodiaco
dia=int(input())
mes=int(input())

fecha=(mes*100+dia)

if 120<fecha<=219:
    print("Acuario")
elif 219<fecha<=320:
    print("Piscis")
elif 320<fecha<=420:
    print("Aries")
elif 420<fecha<=521:
    print("Tauro")
elif 521<fecha<=621:
    print("Geminis")
elif 621<fecha<=722:
    print("Cancer")
elif 722<fecha<=822:
    print("Leo")
elif 822<fecha<=923:
    print("Virgo")
elif 923<fecha<=1023:
    print("Libra")
elif 1023<fecha<=1122:
    print("Scorpio")
elif 1122<fecha<=1221:
    print("Sagitario")
else:
    print("Capricornio")
