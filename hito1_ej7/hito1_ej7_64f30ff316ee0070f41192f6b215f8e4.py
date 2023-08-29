dia=eval(input("Ingrese dia de Nacimiento: "))
mes=eval(input("Ingrese mes de Nacimiento: "))

if mes==1:
    if dia<20:
        signo='Capricornio'
    else:
        signo='Acuario'
elif mes==2:
    if dia<19:
        signo='Acuario'
    else:
        signo='Picis'
elif mes==3:
    if dia<21:
        signo='Picis'
    else:
        signo='Aries'
elif   mes==4:
    if dia<20:
        signo='Aries'
    else:
        signo='Tauro'
elif   mes==5:
    if dia<21:
        signo='Tauro'
    else:
        signo='Geminis'
elif   mes==6:
    if dia<21:
        signo='Geminis'
    else:
        signo='Cancer'
elif   mes==7:
    if dia<23:
        signo='Cancer'
    else:
        signo='Leon'
elif   mes==8:
    if dia<23:
        signo='leon'
    else:
        signo='Virgo'
elif   mes==9:
    if dia<23:
        signo='Virgo'
    else:
        signo='libra'
elif   mes==10:
    if dia<23:
        signo='Libra'
    else:
        signo='Escorpion'
elif   mes==11:
    if dia<23:
        signo='Escorpion'
    else:
        signo='Sagitario'
elif   mes==12:
    if dia<22:
        signo='Sagitario'
    else:
        signo='Capricornio'

print(signo)