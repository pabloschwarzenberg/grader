#Zodiaco
a =int(input("ingrese su dia de nacimiento: "))
b =int(input("ingrese su mes de nacimiento solo del 1-12: "))
if(a >= 21 and b == 3) or ( a <= 20 and b == 4):
    print("aries")
elif(a >= 21 and b == 4) or (a <= 21 and b == 5):
    print("tauro")
elif(a >= 22 and b == 5) or (a <= 21 and b == 6):
    print("geminis")
elif(a >= 22 and b == 6) or (a <= 22 and b == 7):
    print("cancer")
elif(a >= 23 and b == 7) or (a <= 23 and b == 8):
    print("leo")
elif(a >= 24 and b == 8) or (a <= 23 and b == 9):
    print("virgo")
elif(a >= 24 and b == 9) or (a <= 23 and b == 10):
    print("libra")
elif(a >= 24 and b == 10) or (a <= 22 and b == 11):
    print("escorpio")
elif(a >= 23 and b == 11) or (a <= 21 and b == 12):
    print("sagitario")
elif(a >= 22 and b == 12) or (a <= 20 and b == 1):
    print("capricornio")
elif(a >= 21 and b == 1) or (a <= 18 and b == 2):
    print("acuario")
elif(a >= 19 and b == 2) or (a <= 20 and b == 3):
    print("piscis")