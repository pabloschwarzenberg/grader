#Zodiaco
dia=int(input('ingrese dia de nacimiento:'))
mes=int(input('ingrese mes de nacimineto:'))


if (mes==3 and 1<=dia<=22) or (mes==4 and 1<=dia<=20):
    print('aries')

if (mes==4 and 21<=dia<=30) or (mes==5 and 1<=dia<=21):
    print('tauro')

if (mes==5 and 22<=dia<=30) or (mes==4 and 1<=dia<=21):
    print('geminis')

if (mes==6 and 21<=dia<=30) or (mes==7 and 1<=dia<=23):
    print('cancer')

if (mes==7 and 24<=dia<=30) or (mes==8 and 1<=dia<=23):
    print('león')

if (mes==8 and 24<=dia<=30) or (mes==9 and 1<=dia<=23):
    print('virgo')

if (mes==9 and 24<=dia<=30) or (mes==10 and 1<=dia<=16):
    print('libra')

if (mes==10 and 24<=dia<=30) or (mes==11 and 1<=dia<=22):
    print('escorpión')

if (mes==11 and 23<=dia<=30) or (mes==12 and 1<=dia<=22):
    print('sagitario')

if (mes==12 and 23<=dia<=30) or (mes==1 and 1<=dia<=20):
    print('capricornio')

if (mes==1 and 20<=dia<=30) or (mes==2 and 1<=dia<=19):
    print('acuario')

if (mes==2 and 20<=dia<=30) or (mes==3 and 1<=dia<=21):
    print('piscis')
