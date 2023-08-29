#Zodiaco
dia=int(input())
mes=int(input())
if mes==3:
    if dia<=20:
        print("picis")
    elif 21<=dia<=31:
        print("aries")
elif mes==4:
    if 21<=dia<=30:
        print("tauro")
    elif dia<=20:
        print("aries")        
elif mes==5:
    if dia<=21:
        print("tauro")
    elif 21<dia<=31:
        print("gemenis")
elif mes==6:
    if dia<=21:
        print("gemenis")
    elif 22<=dia<=30:
        print("cancer")
elif mes==7:
    if dia<=22:
        print("cancer")
    elif 23<=dia<=31:
        print("leo")
elif mes==8:
    if dia<=22:
        print("leo")
    elif 23<=dia<=31:
        print("virgo")
elif mes==9:
    if dia<=23:
        print("virgo")
    elif 24<=dia<=30:
        print("libra")
elif mes==10:
    if dia<=23:
        print("libra")
    elif 24<=dia<=31:
        print("escorpion")
elif mes==11:
    if dia<=22:
        print("escorpion")
    elif 23<=dia<=30:
        print("saguitario")
elif mes==12:
    if dia<=21:
        print("saguitario")
    elif 22<=dia<=31:
        print("capricornio")
elif mes==1:
    if dia<=20:
        print("capricornio")
    elif 21<=dia<=30:
        print("acuario")
elif mes==2:
    if dia<=19:
        print("acuario")
    elif 20<=dia<=29:
        print("picis")
        