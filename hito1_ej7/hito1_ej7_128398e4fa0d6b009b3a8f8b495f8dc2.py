#Zodiaco
# Entradas


day = int(input("Ingrese su dia de nacimiento(numero): "))
month = int(input("Ingrese su mes de nacimiento(numero): "))

if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
    print("aries")
elif (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 20):
    print("tauro")
elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 21):
    print("geminis")
elif (month == 6 and 22 <= day <= 31) or (month == 7 and 1 <= day <= 21):
    print("cancer")
elif (month == 7 and 22 <= day <= 31) or (month == 8 and 1 <= day <= 22):
    print("leo")
elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
    print("virgo")
elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 22):
    print("libra")
elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 22):
    print("escorpio")
elif (month == 11 and 23 <= day <= 31) or (month == 12 and 1 <= day <= 21):
    print("sagitario")
elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 20):
    print("capricornio")
elif (month == 1 and 21 <= day <= 31) or (month == 2 and 1 <= day <= 19):
    print("acuario")
elif (month == 2 and 20 <= day <= 28) or (month == 3 and 1 <= day <= 20):
    print("piscis")
        