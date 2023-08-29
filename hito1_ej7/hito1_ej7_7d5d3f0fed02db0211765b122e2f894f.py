#Zodiaco
d = eval(input())
m = eval(input())
signo = 0
if m == 1:
    if d < 21:
        signo = "Capricornio"
    else:
        signo = "Aquario"
elif m == 2:
    if d < 19:
        signo = "Aquario"
    else:
        signo = "Picis"
elif m == 3:
    if d < 21:
        signo = "Picis"
    else:
        signo = "Aries"
elif m == 4:
    if d < 21:
        signo = "Aries"
    else:
        signo = "Tauro"
elif m == 5:
    if d < 21:
        signo = "Tauro"
    else:
        signo = "Géminis"
elif m == 6:
    if d < 22:
        signo = "Géminis"
    else:
        signo = "Cáncer"
elif m == 7:
    if d < 23:
        signo = "Cáncer"
    else:
        signo = "Leo"
elif m == 8:
    if d < 23:
        signo = "Leo"
    else:
        signo = "Virgo"
elif m == 9:
    if d < 23:
        signo = "Virgo"
    else:
        signo = "Libra"
elif m == 10:
    if d < 23:
        signo = "Libra"
    else:
        signo = "Escorpio"
elif m == 11:
    if d < 23:
        signo = "Escorpio"
    else:
        signo = "Sagitario"
elif m == 12:
    if d < 22:
        signo = "Sagitario"
    else:
        signo = "Capricornio"
print(signo)