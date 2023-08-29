d=int(input("ingresa el dia: "))
m=int(input("ingresa el mes: "))
if m==1 and d>=20 or m==2 and d>=19:
    print("ACUARIO")
elif m==2 and d>=20 or m==3 and d>=20:
    print("PICIS")
elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
        print("Aries")
elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
        print("Tauro")
elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
        print("Géminis")
elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
        print("Cáncer")
elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
        print("Leo")
elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        print("Virgo")
elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
        print("Libra")
elif (m == 10 and d >= 23) or (m == 11 and d <= 21):
        print("Escorpio")
elif (m == 11 and d >= 22) or (m == 12 and d <= 21):
        print("Sagitario")
else:
        print("Capricornio")