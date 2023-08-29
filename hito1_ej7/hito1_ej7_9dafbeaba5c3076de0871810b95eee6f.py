#Zodiaco
día=int(input("Ingrese su día de nacimiento: "))
mes=int(input("Ingrese su número de mes de nacimiento: "))

if mes == 3 and día >= 21 or mes == 4 and día <=20:
    print("ARIES")
elif mes == 4 and día >= 21 or mes == 5 and día <= 20:
    print("TAURO")
elif mes == 5 and día >= 21 or mes == 6 and día <=20:
    print("GEMINIS")
elif mes == 6 and día >= 21 or mes == 7 and día <= 22:
    print("CANCER")
elif mes == 7 and día >= 23 or mes == 8 and día <= 22:
    print("LEO")
elif mes == 8 and día >= 23 or mes == 9 and día <= 22:
    print("VIRGO")
elif mes == 9 and día >= 23 or mes == 10 and día <= 22:
    print("LIBRA")
elif mes == 10 and día >= 23 or mes == 11 and día <= 21:
    print("ESCORPION")
elif mes == 11 and día >= 22 or mes == 12 and día <= 21:
    print("SAGITARIO")
elif mes == 12 and día >= 22 or mes == 1 and día <= 19:
    print("CAPRICORNIO")
elif mes == 1 and día >= 20 or mes == 2 and día <= 18:
    print("ACUARIO")
elif mes == 2 and día >= 19 or mes == 3 and día <= 20:
    print("PISCIS")


      