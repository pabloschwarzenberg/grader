#Zodiaco
x = int(input("introduce el dia de tu cumoleaños: "))
y = int(input("introduce el mes de tu cumpleaños: "))

if x >= 21 and y == 3 or x <= 20 and y == 4:
    print("aries")
elif x >= 20 and y == 4 or x <= 21 and y == 5:
    print("tauro")
elif x >= 21 and y == 5 or x <= 21 and y == 6:
    print("geminis")
elif x >= 21 and y == 6 or x <= 20 and y == 7:
    print("cáncer")
elif x >= 21 and y == 7 or x <= 20 and y == 8:
    print("león")
elif x >= 21 and y == 8 or x <= 20 and y == 9:
    print("virgo")
elif x >= 21 and y == 9 or x <= 20 and y == 10:
    print("libra")
elif x >= 21 and y == 10 or x <= 20 and y == 11:
    print("escorpión")
elif x >= 21 and y == 11 or x <= 20 and y == 12:
    print("sagitario")
elif x >= 21 and y == 12 or x <= 20 and y == 1:
    print("capricornio")
elif x >= 21 and y == 1 or x <= 20 and y == 2:
    print("acuario")
elif x >= 21 and y == 2 or x <= 20 and y == 3:
    print("piscis")
else:
    print("están malos los datos")
