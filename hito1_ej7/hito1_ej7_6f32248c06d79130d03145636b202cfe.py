#Zodiaco
a = int(input("dia: "))
b = int(input("Mes: "))
if ( 19<=a or a>=21 )and ( b == 3 or b == 4):
    print("Eres aries")
elif ( 19<=a or a>=20 )and ( b == 4 or b == 5):
    print("Eres tauro")
elif ( 20>=a or a>=21 ) and ( b == 5 or b == 6):
    print("Eres gemenis")
elif ( 21<=a or a<=22 ) and ( b == 6 or b == 7):
    print("Eres cancer")
elif ( 22>=a or a>=23 ) and ( b == 7 or b == 8):
    print("Eres leo")
elif ( 22>=a or a>=23 ) and ( b == 8 or b == 9):
    print("Eres virgo")
elif ( 22>=a or a>=23 ) and ( b == 9 or b == 10):
    print("Eres libra")
elif ( 21>=a or a<=23 ) and ( b == 10 or b == 11):
    print("Eres escorpio")
elif ( 22<=a or a<=21 ) and ( b == 11 or b == 12):
    print("Eres sagitario")
elif ( 19>=a or a>=22) and ( b == 12 or b == 1):
    print("Eres capricornio")
elif ( 18>=a or a>=20 ) and ( b == 6 or b == 2):
    print("Eres acuario")
else:
    if ( 19<=a or a<=20 ) and ( b == 2 or b == 3):
        print("Eres picis")
    