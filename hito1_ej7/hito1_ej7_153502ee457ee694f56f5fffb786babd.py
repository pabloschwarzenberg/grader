#Zodiaco
dia=int(input("ingrse su dia de nacimiento:"))
mes=int(input("ingrese su mes de nacimiento:"))

if mes==1 and 20<dia<=31 or mes==2 and 0<=dia<=19:
    print("acuario")
elif mes==2 and 19<dia<=28 or mes==3 and 0<=dia<=21:
    print("piscis")
elif mes==3 and 21<dia<=31 or mes==4 and 0<=dia<=20:
    print("aries")
elif mes==4 and 20<dia<=30 or mes==5 and 0<=dia<=21:
    print("tauro")
elif mes==5 and 21<dia<=31 or mes==6 and 0<=dia<=21:
    print("geminis")
elif mes==6 and 21<dia<=30 or mes==7 and 0<=dia<=23:
    print("cancer")
elif mes==7 and 23<dia<=31 or mes==8 and 0<=dia<=23:
    print("leon")
elif mes==8 and 23<dia<=30 or mes==9 and 0<=dia<=23:
    print("virgo")
elif mes==9 and 23<dia<=31 or mes==10 and 0<=dia<=23:
    print("libra")
elif mes==10 and 23<dia<=30 or mes==11 and 0<=dia<=22:
    print("escorpion")
elif mes==11 and 22<dia<=31 or mes==12 and 0<=dia<=22:
    print("sagitario")
elif mes==12 and 22<dia<=31 or mes==6 and 0<=dia<=20:
    print("capricornio")      