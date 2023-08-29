#Zodiaco
dia = int(input("digite el dia de su cumpleaños ")) 
mes = int(input("digite su mes de cumpleaños en numero: "))


Ar = "Aries"
Ta = "Taurus"
Ge = "Gemini"
Ca = "Cancer"
Le = "Leo"
Vir = "Virgo"
Lib = "Libra"
Sco = "Scorpio"
Sag = "sagitario"
Cap = "Capricorn"
Aq = "Aquarius"
Pis = "Pisces"

if mes == 3 and dia >= 21 or mes == 4 and dia <= 20:
    print("Su signo es:", Ar )

elif mes == 4 and dia >= 20 or mes == 5 and dia <= 21:
    print("Su signo es:", Ta )

elif mes == 5 and dia >= 21 or mes == 6 and dia <= 21:
    print("Su signo es:", Ge)

elif mes == 6 and dia >= 21 or mes == 7 and dia <= 23:
    print("Su signo es:", Ca)

elif mes == 7 and dia >= 23 or mes == 8 and dia <= 23:
    print("Su signo es:", Le)

elif mes == 8 and dia >= 23 or mes == 9 and dia <= 23:
    print("Su signo es:", Vir)

elif mes == 9 and dia >= 23 or mes == 10 and dia <= 23:
    print("Su signo es:", Lib)

elif mes == 10 and dia >= 23 or mes == 11 and dia <= 22:
    print("Su signo es:", Sco)

elif mes == 11 and dia >= 23 or mes == 12 and dia <= 22:
    print("Su signo es:", Sag)

elif mes == 12 and dia >= 22 or mes == 1 and dia <= 20:
    print("Su signo es:", Cap)

elif mes == 1 and dia >= 20 or mes == 2 and dia <= 19:
    print("Su signo es:", Aq)

elif mes == 2 and dia >= 19 or mes == 3 and dia <= 21:
    print("Su signo es:", Pis)

else:
    print("Signo incorrecto")   