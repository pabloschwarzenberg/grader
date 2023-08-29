dia=int(input())
mes=int(input())
if (mes==3 and 21<=dia) or (mes==4 and dia<=20):
    print("Aries")
elif (mes==4 and 21<=dia) or (mes==5 and dia<=21):
    print("Tauro")
elif (mes==5 and 22<=dia) or (mes==6 and dia<=21):
    print("Geminis")
elif (mes==6 and 22<=dia) or (mes==7 and dia<=22):
    print("cancer")
elif (mes==7 and 23<=dia) or (mes==8 and dia<=22):
    print("Leo")
elif (mes==8 and 23<=dia) or (mes==9 and dia<=23):
    print("Virgo")
elif (mes==9 and 24<=dia) or (mes==10 and dia<=23):
    print("Libra")
elif (mes==10 and 24<=dia) or (mes==11 and dia<=22):
    print("Escorpión")
elif (mes==11 and 23<=dia) or (mes==12 and dia<=21):
    print("Sagitario")
elif (mes==12 and 22<=dia) or (mes==1 and dia<=20):
    print("Capricornio")
elif (mes==1 and 21<=dia) or (mes==2 and dia<=19):
    print("Acuario")
elif (mes==2 and 20<=dia) or (mes==3 and dia<=20):
    print("Piscis")      