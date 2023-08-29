#Zodiaco
def dia(a,b,c):# "a" dia de inicio "b" dia de termino
    if day>=a and day<=b:
        print(c)
        
        
day = int(input('ingrese su dia de nacimiento: '))
month = int(input('introdusca su mes de nacimiento:'))

if month == 1:#enero
    dia(1,20,'capricornio')
    dia(21,31,'acuario')
elif month == 2:#febrero
    dia(1,19,'acuario')
    dia(20,29,'pisis')
elif month == 3:#marzo
    dia(1,21,'pisis')
    dia(22,31,'aries')
elif month == 4:#abril
    dia(1,20,'aries')
    dia(21,31,'tauro')
elif month == 5:
    dia(1,21,'tauro')
    dia(22,31,'geminis')
elif month == 6:#junio
    dia(1,21,'geminis')
    dia(22,30,'cancer')
elif month == 7:#julio
    dia(1,23,'cancer')
    dia(24,31,'leo')
elif month == 8:#agosto
     dia(1,23,'leo')
     dia(24,31,'virgo')
elif month == 9:#septiembre
     dia(1,23,'virgo')
     dia(24,30,'libra')
elif month == 10:#octubre
     dia(1,23,'libra')
     dia(24,31,'escorpio')
elif month == 11:#noviembre
     dia(1,22,'escorpio')
     dia(23,30,'sagitario')
elif month == 12:#diciembre
     dia(1,22,'sagitario')
     dia(23,31,'capricornio')
else:
    print('introdusca un mes valido')
     