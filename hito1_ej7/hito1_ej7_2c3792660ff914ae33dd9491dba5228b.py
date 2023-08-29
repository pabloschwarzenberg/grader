#Zodiaco
  
n=int(input("dia de cumpleaños:"))
m=int(input("mes de cumpleaños:"))

if 21<=n<=31 and m==3 or 1<=n<=20 and m==4:
    print("Aries")
elif 21<=n<=30 and m==4 or 1<=n<=21 and m==5:
    print("Tauro")
elif 22<=n<=31 and m==5 or 1<=n<=21 and m==6:
    print("Geminis")
elif 22<=n<=30 and m==6 or 1<=n<=22 and m==7:
    print("Cancer")
elif 23<=n<=31 and m==7 or 1<=n<=22 and m==8:
    print("Leo")
elif 23<=n<=31 and m==8 or 1<=n<=23 and m==9:
    print("Virgo")
elif 24<=n<=30 and m==9 or 1<=n<=23 and m==10:
    print("Libra")
elif 24<=n<=31 and m==10 or 1<=n<=22 and m==11:
    print("Escorpion")
elif 23<=n<=30 and m==11 or 1<=n<=21 and m==12:
    print("Sagiatrio")
elif 22<=n<=31 and m==12 or 1<=n<=20 and m==1:
    print("Capricornio")
elif 21<=n<=31 and m==1 or 1<=n<=19 and m==2:
    print("Acuario")
else:
    print("Piscis")
