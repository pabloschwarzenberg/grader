n1=int(input("Ingrese Dia de cumpleaños :"))
n2=int(input("Ingrese el mes de cumpleaños :"))

if (n1 >= 21) and (n2==3) or (n1<20) and (n2==4):
    print("Aries ")
elif (n1>=20) and (n2==4) or (n1<21) and (n2==5):
    print("Taurus")
elif(n1>=21) and (n2==5) or (n2==6):
    print("Geminis")
elif(n1>=21) and (n2==6) or (n1<23) and (n2==7):
    print("Cancer")
elif(n1>=23) and (n2==7) or (n1<23) and (n2==8):
    print("Leo")
elif(n1>=23) and (n2==8) or (n1<23) and (n2==9):
    print("Virgo")
elif(n1>=23)and (n2==9) or (n1 <23) and (n2==10):
    print("Libra")
elif(n1<=23) and (n2==10)or(n2<23) and (n2==11):
    print("escorpio")
elif (n1>=23) and (n2==11) or (n1<22) and (n2==12):
    print("Sagittaurius")
elif (n1>=22) and (n2==12) or (n1<=20) and (n2==1):
    print("capricornio")
elif (n1>=20) and (n2==1) or (n1<=19) and (n2==2):
    print("acuario")
elif (n1<=19) and (n2==2) or (n1==21) and (n2==3):
    print("piscis")