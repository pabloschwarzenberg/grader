#Zodiaco
 #Entrada
dia = int(input("Ingrese su dia de nacimiento: "))
mes = input("Ingrese su mes de nacimiento: ")

#Clasificacíon 
if mes == "1" and dia >= 21 or mes == "2" and dia <= 18:
    print("Su signo Zodiacal es Acuario")
elif mes == "2" and dia >= 19 or mes == "3" and dia <= 20:
    print("Su signo Zodiacal es Piscis")
elif mes == "3" and dia >= 21 or mes == "4" and dia <= 20:
    print("Su signo Zodiacal es Aries")
elif mes == "4" and dia >= 21 or mes == "5" and dia <= 20:
    print("Su signo Zodiacal es Tauro")
elif mes== "5" and dia >= 21 or mes == "6" and dia <= 21:
    print("Su signo Zodiacal es Geminis")
elif mes == "6" and dia >= 22 or mes == "7" and dia <= 22:
    print("Su signo Zodiacal es Cancer")
elif mes == "7" and dia >= 23 or mes == "8" and dia <= 22:
    print("Su signo Zodiacal es Leo")
elif mes == "8" and dia >= 23 or mes == "9" and dia <= 22:
    print("Su signo Zodiacal es Virgo")
elif mes == "9" and dia >= 23 or mes == "10" and dia <= 22:
    print("Su signo Zodiacal es Libra")
elif mes == "10" and dia >= 23 or mes == "11" and dia <= 22:
    print("Su signo Zodiacal es Escorpio")
elif mes == "11" and dia >=23 or mes == "12" and dia <= 21:
    print("Su signo Zodiacal es Sagitario")
elif mes == "12" and dia >=22 or mes == "1" and dia <= 20:
    print("Su signo Zodiacal es Capricornio")
    