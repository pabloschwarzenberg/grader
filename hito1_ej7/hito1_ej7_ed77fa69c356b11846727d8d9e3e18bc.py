#Zodiaco
d = int(input("Ingrese su día de nacimiento:"))
m = int(input("Ingrese su mes de nacimiento:"))

if m == 3 and 31 >= d >= 21 or m == 4 and 20 >= d >= 1:
    print("ARIES")

elif m == 4 and 30 >= d >= 21 or m == 5 and 21 >= d >= 1:
    print("TAURUS")

elif m == 5 and 31 >= d >= 22 or m == 6 and 21 >= d >= 1:
    print("GEMINIS")

elif m == 6 and 30 >= d >= 22 or m == 7 and 22 >= d >= 1:
    print("CANCER")

elif m == 7 and 31 >= d >= 23 or m == 8 and 22 >= d >= 1:
    print("LEO")

elif m == 8 and 31 >= d >= 23 or m == 9 and 23 >= d >= 1:
    print("VIRGO")

elif m == 9 and 30 >= d >= 24 or m == 10 and 23 >= d >= 1:
    print("LIBRA")

elif m == 10 and 31 >= d >= 24 or m == 11 and 22 >= d >= 1:
    print("SCORPIO")

elif m == 11 and 30 >= d >= 23 or m == 12 and 21 >= d >= 1:
    print("SAGITTARIUS")

elif m == 12 and 31 >= d >= 22 or m == 1 and 20 >= d >= 1:
    print("CAPRICORNIO")

elif m == 1 and 31 >= d >= 21 or m == 2 and 19 >= d >= 1:
    print("AQUARIUS")

elif m == 2 and 29 >=d >= 20 or m == 3 and 20 >= d >= 1:
    print("PISCES")

else:
    print("La fecha ingresada no está correcta")
    



