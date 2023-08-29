#Zodiaco
dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))

if 21 <= dia <= 31 and mes == 3 or 1 <= dia <= 20 and mes == 4:
    print("Eres Aries")
elif 21 <= dia <= 30 and mes == 4 or 1 <= dia <= 20 and mes == 5:
    print("Eres Tauro")
elif 21 <= dia <= 31 and mes == 5 or 1 <= dia <= 21 and mes  == 6:
    print("Eres Géminis")
elif 22 <= dia <= 30 and mes == 6 or 1 <= dia <= 22 and mes == 7:
    print("Eres Cáncer")
elif 23 <= dia <= 31 and mes == 7 or 1 <= dia <= 22 and mes == 8:
    print("Eres Leo")
elif 23 <= dia <= 31 and mes == 8 or 1 <= dia <= 22 and mes == 9:
    print("Eres Virgo")
elif 23 <= dia <= 30 and mes == 9 or 1 <= dia <= 22 and mes == 10:
    print("Eres Libra")
elif 23 <= dia <= 31 and mes == 10 or 1 <= dia <= 22 and mes == 11:
    print("Eres Escorpio")
elif 23 <= dia <= 30 and mes == 11 or 1 <= dia <= 21 and mes == 12:
    print("Eres Sagitario")
elif 22 <= dia <= 31 and mes == 12 or 1 <= dia <= 20 and mes == 1:
    print("Eres Capricornio")
elif 21 <= dia <= 31 and mes == 1 or 1 <= dia <= 18 and mes == 2:
    print("Eres Acuario")
elif 19 <= dia <= 28 and mes == 2 or 1 <= dia <= 20 and mes == 3:
    print("Eres Piscis")
