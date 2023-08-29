n=input()
m=n[2:]
d=n[:2]
signo=""
mes_nacimiento = m[1:]
dia_nacimiento = int(d)
if mes_nacimiento == 1:
    if dia_nacimiento <= 20:
        signo = "capricornio"
    else:
        signo = "acuario"
elif mes_nacimiento == 2:
    if dia_nacimiento <= 18:
        signo = "acuario"
    else:
        signo = "piscis"
elif mes_nacimiento == 3:
    if dia_nacimiento <= 20:
        signo = "piscis"
    else:
        signo = "aries"
elif mes_nacimiento == 4:
    if dia_nacimiento <= 20:
        signo = "aries"
    else:
        signo = "tauro"
elif mes_nacimiento == 5:
    if dia_nacimiento <= 21:
        signo = "tauro"
    else:
        signo = "geminis"
elif mes_nacimiento == 6:
    if dia_nacimiento <= 21:
        signo = "geminis"
    else:
        signo = "cancer"
elif mes_nacimiento == 7:
    if dia_nacimiento <= 22:
        signo = "cancer"
    else:
        signo = "leo"
elif mes_nacimiento == 8:
    if dia_nacimiento <= 23:
        signo = "leo"
    else:
        signo = "virgo"
elif mes_nacimiento == 9:
    if dia_nacimiento <= 23:
        signo = "virgo"
    else:
        signo = "libra"
elif mes_nacimiento == 10:
    if dia_nacimiento <= 23:
        signo = "libra"
    else:
        signo = " escorpio"
elif mes_nacimiento == 11:
    if dia_nacimiento <= 22:
        signo = " escorpio"
    else:
        signo = "sagitario"
elif mes_nacimiento == 12:
    if dia_nacimiento <= 21:
        signo = "sagitario"
    else:
        signo = "capricornio"

print("el signo es",signo)

