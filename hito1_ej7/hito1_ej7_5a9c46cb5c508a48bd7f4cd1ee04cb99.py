d=int(input())
m=int(input())

if m==2:
    d+=31
if m==3:
    d+=59
if m==4:
    d+=90
if m==5:
    d+=120
if m==6:
    d+=151
if m==7:
    d+=181
if m==8:
    d+=211
if m==9:
    d+=242
if m==10:
    d+=272
if m==11:
    d+=303
if m==12:
    d+=333

if 80<=d<=110:
    print('Aries')
if 111<=d<=141:
    print('Tauro')
if 142<=d<=172:
    print('Geminis')
if 173<=d<=203:
    print('Cancer')
if 204<=d<=233:
    print('Leo')
if 234<=d<=265:
    print('Virgo')
if 266<=d<=295:
    print('Libra')
if 296<=d<=325:
    print('Escorpion')
if 326<=d<=354:
    print('Sagitario')
if 355<=d<=365 or 1<=d<=20:
    print('Capricornio')
if 21<=d<=50:
    print('Acuario')
if 51<=d<=79:
    print('Piscis')
