#Zodiaco
a=int(input("Ingrese su dia de nacimiento: "))
b=int(input("Ingrese su mes de nacimiento solo con numeros del 1-12: "))
if(a >= 21 and b == 3) or ( a <= 20 and b == 4):
    print("Aries")
elif(a >= 21 and b == 4) or (a <= 21 and b == 5):
    print("Tauro")
elif(a >= 22 and b == 5) or (a <= 21 and b == 6):
    print("Geminis")
elif(a >= 22 and b == 6) or (a <= 22 and b == 7):
    print("Cancer")
elif(a >= 23 and b == 7) or (a <= 23 and b == 8):
    print("Leo")
elif(a >= 24 and b == 8) or (a <= 23 and b == 9):
    print("Virgo")
elif(a >= 24 and b == 9) or (a <= 23 and b == 10):
    print("Libra")
elif(a >= 24 and b == 10) or (a <= 22 and b == 11):
    print("Escorpio")
elif(a >= 23 and b == 11) or (a <= 21 and b == 12):
    print("Sagitario")
elif(a >= 22 and b == 12) or (a <= 20 and b == 1):
    print("Capricornio")
elif(a >= 21 and b == 1) or (a <= 18 and b == 2):
    print("Acuario")
elif(a >= 19 and b == 2) or (a <= 20 and b == 3):
    print("Piscis")