#Zodiaco
print('Por favor, ingresa día y mes de nacimiento:')
d=int(input('Día: '))
m=int(input('Mes: '))

if (21<=d<=31 and m==3) or (1<=d<=20 and m==4):
    print('Aries')
elif (20<=d<=30 and m==4) or (1<=d<=20 and m==5):
    print('Tauro')
elif (21<=d<=31 and m==5) or (1<=d<=21 and m==6):
    print('Geminis')
elif (21<d<=30 and m==6) or (1<=d<=23 and m==7):
    print('cancer')
elif (23<d<=31 and m==7) or (1<=d<=23 and m==8):
    print('León')
elif (23<d<=31 and m==8) or (1<=d<=23 and m==9):
    print('Virgo')
elif (23<d<=30 and m==9) or (1<=d<=23 and m==10):
    print('Libra')
elif (23<d<=31 and m==10) or (1<=d<=22 and m==11):
    print('Escorpio')
elif (22<d<=30 and m==11) or (1<=d<=22 and m==12):
    print('Sagitario')
elif (22<d<=31 and m==12) or (1<=d<=20 and m==1):
    print('Capricornio')
elif (20<d<=31 and m==1) or (1<=d<=19 and m==2):
    print('Acuario')
elif (19<d<=29 and m==2) or (1<=d<=21 and m==3):
    print('Piscis')