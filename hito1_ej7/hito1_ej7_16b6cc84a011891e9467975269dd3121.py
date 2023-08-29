dia = eval(input('ingresar dia: '))
mes = eval(input('ingresar mes: '))

if mes==1 and 19<dia>31 or mes==2 and 1<=dia<20:
    print('Acuario')

if mes==2 and 18<dia>30 or mes==3 and 1<=dia<22:
    print('Piscis')

if mes==3 and 20<dia>30 or mes==4 and 1<=dia<21:
    print('Aries')

if mes==4 and 19<dia>31 or mes==5 and 1<=dia<22:
    print('Tauro')

if mes==5 and 20<dia>32 or mes==6 and 1<=dia<22:
    print('Géminis')

if mes==6 and 20<dia>31 or mes==7 and 1<=dia<24:
    print('Cáncer')

if mes==7 and 22<dia>32 or mes==8 and 1<=dia<24:
    print('Leo')

if mes==8 and 22<dia>31 or 8<=mes<=9 and 1<=dia<24:
    print('Virgo')


if mes==9 and 23<dia>31 or mes==10 and 1<=dia<24:
    print('Libra')


if mes==10 and 22<dia<32 or mes==11 and 1<=dia<23:
    print('Escorpio')


if mes==11 and 21<dia>30 or mes==12 and 1<=dia<23:
    print('Sagitario')


if mes==12 and 21<dia>32 or mes==1 and 1<=dia<21: 
    print('Capricornio')
