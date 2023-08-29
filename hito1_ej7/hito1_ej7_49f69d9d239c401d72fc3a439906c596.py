#Zodiaco
dia = int(input('dia: '))
mes = int(input('mes: '))
signo = ''

if mes == 1:
    if dia >= 21:
        signo = 'Acuario'
    else:
        signo = 'Capricornio'

elif mes == 2:
    if dia >= 20:
        signo = 'Piscis'
    else:
        signo = 'Acuario'

elif mes == 3:
    if dia >= 21:
        signo = 'Aries'
    else:
        signo = 'Piscis'

elif mes == 4:
    if dia >= 21:
        signo = 'Tauro'
    else:
        signo = 'Aries'

elif mes == 5:
    if dia >= 21:
        signo = 'Geminis'
    else:
        signo = 'Tauro'

elif mes == 6:
    if dia >= 21:
        signo = 'Cancer'
    else:
        signo = 'Geminis'

elif mes == 7:
    if dia >= 22:
        signo = 'Leo'
    else:
        signo = 'Cancer'

elif mes == 8:
    if dia >= 22:
        signo = 'Virgo'
    else:
        signo = 'Leo'

elif mes == 9:
    if dia >= 22:
        signo = 'Libra'
    else:
        signo = 'Virgo'

elif mes == 10:
    if dia >= 22:
        signo = 'Scorpio'
    else:
        signo = 'Libra'

elif mes == 11:
    if dia >= 22:
        signo = 'Sagitario'
    else:
        signo = 'Escorpio'

elif mes == 12:
    if dia >= 22:
        signo = 'Capricornio'
    else:
        signo = 'Sagitario'

print(signo)