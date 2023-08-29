#Zodiaco

x=int(input('dia de nacimiento:'))
y=int(input('mes de nacimiento:'))
if ((21<=x) and (3==y))or ((x<=20) and (y==4)):
    print('aries')
if ((21<=x)and(y==4)) or ((x<=21) and (y==5)):
    print('tauro')
if ((x>=22)and(y==5)) or ((x<=21) and (y==6)):
    print('geminis')
if ((x>=22) and (y==6)) or ((x<=23) and (y==7)):
    print('cancer')
if ((24<=x)and(y==7)) or ((23>=x) and(y==8)):
    print('leo')
if ((24<=x)and(y==8))or(23>=x)and(y==9):
    print('virgo')
if ((24<=x)and(y==9))or((23>=x)and(y==10)):
    print('libra')
if ((x>=24)and(y==10))or ((x<=22)and(y==11)):
    print('escorpio')
if ((x>=23)and(y==11)) or ((x<=22) and(y==12)):
    print('sagitario')
if ((x>=23)and(y==12)) or ((x<=20)and(y==1)):
    print('capricornio')
if ((x>=21)and(y==1))or((x<=19)and(y==2)):
    print('acuario')
if ((x>=20)and(y==2)) or ((x<=20)and(y==3)):
    print('piscis')

