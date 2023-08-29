D = int(input("Ingrese el dia de su nacimiento: "))
M = int(input("Ingrese el mes de su nacimiento: "))
signo = "error"
# Aries
if D >= 21 and M == 3 or D <=20 and M == 4:
    signo = "Aries"
# Tauro
elif D >= 21 and M == 4 or D <=20 and M == 5:
    signo = "Tauro"
# Geminis
elif D >= 21 and M == 5 or D <=21 and M == 6:
    signo = "Geminis"
# Cancer
elif D >= 22 and M == 6 or D <=22 and M == 7:
    signo = "Cancer"
# Leo
elif D >= 23 and M == 7 or D <=22 and M == 8:
    signo = "Leo"
# Virgo
elif D >= 23 and M == 8 or D <=22 and M == 9:
    signo = "Virgo"
# Libra
elif D >= 23 and M == 9 or D <=22 and M == 10:
    signo = "Libra"
# Escorpio
elif D >= 23 and M == 10 or D <=22 and M == 11:
    signo = "Escorpio"
# Sagitario
elif D >= 23 and M == 11 or D <=21 and M == 12:
    signo = "Sagitario"
# Capricornio
elif D >= 22 and M == 3 or D <=20 and M == 1:
    signo = "Capricornio"
# Acuario
elif D >= 21 and M == 3 or D <=18 and M == 2:
    signo = "Acuario"
# Piscis
elif D >= 19 and M == 3 or D <=20 and M == 3:
    signo = "Piscis"
print(signo)