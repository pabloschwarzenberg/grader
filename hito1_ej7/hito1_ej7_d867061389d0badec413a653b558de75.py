#Zodiaco
fcd=(int(input("Ingrese el DÍA que está de cumpleaños:" )))
fcm=(int(input("Ingrese el MES en que está de cumpleaños:" )))

if (21<=fcd and fcm==3) or (fcd<=20 and fcm==4):
    print("Aries")
elif (21<=fcd and fcm==4) or (fcd<=21 and fcm==5):
    print("Tauro")
elif (22<=fcd and fcm==5) or (fcd<=21 and fcm==6):
    print("Geminis")
elif (22<=fcd and fcm==6) or (fcd<=22 and fcm==7):
    print("Cancer")
elif (23<=fcd and fcm==7) or (fcd<=22 and fcm==8):
    print("Leo")
elif (23<=fcd and fcm==8) or (fcd<=23 and fcm==9):
    print("Virgo")
elif (24<=fcd and fcm==9) or (fcd<=23 and fcm==10):
    print("Libra")
elif (24<=fcd and fcm==10) or (fcd<=22 and fcm==11):
    print("Escopion")
elif (23<=fcd and fcm==11) or (fcd<=21 and fcm==12):
    print("Sagitario")
elif (22<=fcd and fcm==12) or (fcd<=20 and fcm==1):
    print("Capricornio")
elif (21<=fcd and fcm==1) or (fcd<=19 and fcm==2):
    print("Acuario")
elif (20<=fcd and fcm==2) or (fcd<=20 and fcm==3):
    print("Piscis")  