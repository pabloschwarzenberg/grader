#Zodiaco
import datetime
dia=int(input('ingrese el dia que naciste: '))
mes=int(input('ingrese el mes que naciste : '))
aaaa=2020
fecha=datetime.date(aaaa,mes,dia)

if datetime.date(aaaa,1,20) <= fecha <= datetime.date(aaaa,2,19):
    print('acuario')
elif datetime.date(aaaa,2,19) <=fecha <= datetime.date(aaaa,3,21):
    print('piscis')
elif datetime.date(aaaa,3,21) <= fecha<=datetime.date(aaaa,4,20):
    print('aries')
elif datetime.date(aaaa,4,20) <=fecha<= datetime.date(aaaa,5,21):
    print('tauro')
elif datetime.date(aaaa,5,21) <= fecha <= datetime.date(aaaa,6,21):
    print('jeminis')
elif datetime.date(aaaa,6,21) <=fecha<= datetime.date(aaaa,7,23):
    print('cancer')
elif datetime.date(aaaa,7,23) <= fecha <= datetime.date(aaaa,8,23):
    print('leo')
elif datetime.date(aaaa,8,23) <= fecha <= datetime.date(aaaa,9,23):
    print('virgo')
elif datetime.date(aaaa,9,24) <=fecha<= datetime.date(aaa,10,23):
    print('libra')
elif datetime.date(aaaa,10,23) <= fecha <= datetime.date(aaaa,11,22):
    print('escorpion')
elif datetime.date(aaaa,11,22) <= fecha <= datetime.date(aaa,12,22):
    print('sagitario')
elif datetime.date(aaaa,12,22) <= fecha <= datetime.date(aaaa,1,22):
    print('capricornio')
