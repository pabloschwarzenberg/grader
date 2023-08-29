#Zodiaco
a=int(input("Ingrese su dia de nacimiento: "))
b=int(input("Ingrese su mes de nacimiento: "))

if(b==12 and 22<=a<=31) or (b==1 and 1<=a<=20):
    print("Capricornio")
elif(b==1 and 21<=a<=31) or (b==2 and 1<=a<=19):
    print("Acuario")
elif(b==2 and 20<=a<=28) or (b==3 and 1<=a<=20):
    print("Piscis")
elif(b==3 and 21<=a<=31) or (b==4 and 1<=a<=20):
    print("Aries")
elif(b==4 and 21<=a<=30) or (b==5 and 1<=a<=21):
    print("Tauro")
elif(b==5 and 22<=a<=31) or (b==6 and 1<=a<=21):
    print("Geminis")
elif(b==6 and 22<=a<=31) or (b==7 and 1<=a<=22):
    print("Cancer")
elif(b==7 and 23<=a<=31) or (b==8 and 1<=a<=22):
    print("Leo")
elif(b==8 and 23<=a<=31) or (b==9 and 1<=a<=23):
    print("Virgo")
elif(b==9 and 24<=a<=31) or (b==10 and 1<=a<=23):
    print("Libra")
elif(b==10 and 24<=a<=31) or (b==11 and 1<=a<=22):
    print("Escorpion")
elif(b==11 and 23<=a<=31) or (b==12 and 1<=a<=21):
    print("Sagitario")
