#Zodiaco
print('¿Quieres saber tu signo del zodiaco?')
dia = int(input('Ahora dime el día: '))
mes = int(input('Dime el número del mes en que naciste: '))

if mes==3 and 21<=dia<=31 or mes==4 and 1<=dia<=20:
    print('Tu signo es Aries')
elif mes==4 and 21<=dia<=30 or mes==5 and 1<=dia<=21:
    print('Tu signo es Tauro')
elif mes==5 and 22<=dia<=31 or mes==6 and 1<=dia<=21:
    print('Tu signo es Geminis')
elif mes==6 and 22<=dia<=30 or mes==7 and 1<=dia<=22:
    print('Tu signo es Cáncer')
elif mes==7 and 23<=dia<=31 or mes==8 and 1<=dia<=22:
    print('Tu signo es Leo')
elif mes==8 and 23<=dia<=31 or mes==9 and 1<=dia<=23:
    print('Tu signo es Virgo')
elif mes==9 and 24<=dia<=30 or mes==10 and 1<=dia<=23:
    print('Tu signo es Libra')
elif mes==10 and 24<=dia<=31 or mes==11 and 1<=dia<=22:
    print('Tu signo es Escorpio')
elif mes==11 and 23<=dia<=30 or mes==12 and 1<=dia<=21:
    print('Tu signo es Sagitario')
elif mes==12 and 22<=dia<=31 or mes==1 and 1<=dia<=20:
    print('Tu signo es Capricornio')
elif mes==1 and 21<=dia<=31 or mes==2 and 1<=dia<=19:
    print('Tu signo es Acuario')
elif mes==2 and 20<=dia<=29 or mes==3 and 1<=dia<=20:
    print('Tu signo es Piscis')
else:
    print('Tu fecha de nacimiento es inválida')
