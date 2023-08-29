dia=int(input("Ingrese dia de nacimiento: "))
mes= int(input("Ingrese mes de nacimiento del 1 al 12: "))
while not (dia >0 and dia <=31):
    dia=int(input("Error.... Ingrese dia de nacimiento: "))
while not (mes >0 and mes <=12):
    mes=int(input("Error.... Ingrese mes de nacimiento del 1 al 12: "))
signo = ''
if mes >=1 and mes <=2:
    if dia >=20:
        signo ='Acuario'
    else:
        signo ='Capricornio'
if mes >=2 and mes <=3:
    if dia >=20:
        signo ='Piscis'
    else:
        signo ='Acuario'
if mes >=3 and mes <=4:
    if dia >=21:
        signo ='Aries'
    else:
        signo ='Piscis'
if mes >=4 and mes <=5:
    if dia >=20:
        signo ='Tauro'
    else:
        signo='Aries'
if mes >=5 and mes <=6:
    if dia >=21:
        signo ='Geminis'
    else:
        signo='Tauro'
if mes >=6 and mes <=7:
    if dia >=21:
        signo ='Cancer'
    else:
        signo='Geminis'
if mes >=7 and mes <=8:
    if dia >=23:
        signo ='Leo'
    else:
        signo='Cancer'
if mes >=8 and mes <=9:
    if dia >=23:
        signo ='Virgo'
    else:
        signo='Leo'
if mes >=9 and mes <=10:
    if dia >=23:
        signo ='Libra'
    else:
        signo='Virgo'
if mes >=10 and mes <=11:
    if dia >=23:
        signo ='Escorpion'
    else:
        signo='Libra'
if mes >=11 and mes <=12:
    if dia >=22:
        signo ='Sagitario'
    else:
        signo='Escorpion'

if mes ==1 or mes ==12:
    if mes==1 and dia <=19:
        signo ='Capricornio'
    elif mes ==1 and dia >=20:
        signo='Acuario'
    else:
        signo='Sagitario'
print (signo)