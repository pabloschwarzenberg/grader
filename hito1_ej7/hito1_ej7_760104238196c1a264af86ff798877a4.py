#Zodiaco
dia = int(input())
mes = int(input())

if mes == 1:
    if dia <= 20:
        signo = 'Capricornio'
    else:
        signo = 'Acuario'
elif mes == 2:
    if dia <= 19:
        signo = 'Acuario'
    else:
        signo = 'Pisces'
elif mes == 3:
    if dia <= 21:
        signo = 'Pisces'
    else:
        signo = 'Aries'
elif mes == 4:
    if dia <= 20:
        signo = 'Aries'
    else:
        signo = 'Tauro'
elif mes == 5:
    if dia <= 20:
        signo = 'Tauro'
    else:
        signo = 'Geminis'
elif mes == 6:
    if dia <= 21:
        signo = 'Geminis'
    else:
        signo = 'Cancer'
elif mes == 7:
    if dia <= 21:
        signo = 'Cancer'
    else:
        signo = 'Leo'
elif mes == 8:
    if dia <= 23:
        signo = 'Leo'
    else:
        signo = 'Virgo'
elif mes == 9:
    if dia <= 23:
        signo = 'Virgo'
    else:
        signo = 'Libra'
elif mes == 10:
    if dia <= 22:
        signo = 'Libra'
    else:
        signo = 'Escorpio'
elif mes == 11:
    if dia <= 22:
        signo = 'Escorpio'
    else:
        signo = 'Sagitario'
else:
    if dia <= 21:
        signo = 'Sagitario'
    else:
        signo = 'Capricornio'
print(signo)