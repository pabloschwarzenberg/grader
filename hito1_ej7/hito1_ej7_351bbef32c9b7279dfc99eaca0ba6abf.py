dia = eval(input('Ingrese dia de nacimiento: '))
mes = eval(input('Ingrese mes de nacimiento: '))

if (mes==1 and dia>=20) or (mes==2 and dia<19):
    print('Perteneces al signo de Aquario')
if (mes==2 and dia>=19) or (mes==3 and dia<=21):
    print('Perteneces al signo de Piscis')
if (mes==3 and dia>=21) or (mes==4 and dia<=20):
    print('Perteneces al signo de Aries')
if (mes==4 and dia>=20) or (mes==5 and dia<=21):
    print('Perteneces al signo de Tauro')
if (mes==5 and dia>=21) or (mes==6 and dia<=21):
    print('Perteneces al signo de Gemini')
if (mes==6 and dia>=21) or (mes==7 and dia<=23):
    print('Perteneces al signo de Cancer')
if (mes==7 and dia>=23) or (mes==8 and dia<=23):
    print('Perteneces al signo de Leo')
if (mes==8 and dia>=23) or (mes==9 and dia<=23):
    print('Perteneces al signo de Virgo')
if (mes==9 and dia>=23) or (mes==10 and dia<=23):
    print('Perteneces al signo de Libra')
if (mes==10 and dia>=23) or (mes==11 and dia<=22):
    print('Perteneces al signo de Escorpio')
if (mes==11 and dia>=23) or (mes==12 and dia<22):
    print('Perteneces al signo de Sagitario')
if (mes==12 and dia>=22) or (mes==1 and dia<=20):
    print('Perteneces al signo de Capricornio')      