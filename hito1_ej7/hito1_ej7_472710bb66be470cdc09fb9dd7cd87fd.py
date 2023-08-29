dia_de_nacimiento = int (input ('Ingresar el dia de su cumpleaños: '))
mes_de_nacimiento = int (input ('Ingresar el numero del mes de su cumpleaños: '))
if (dia_de_nacimiento>=21 and mes_de_nacimiento==3) or (dia_de_nacimiento<=20 and mes_de_nacimiento==4):
    print ('Aries')
if (dia_de_nacimiento>=24 and mes_de_nacimiento==9) or (dia_de_nacimiento<=23 and mes_de_nacimiento==10):
    print ('Libra')
if (dia_de_nacimiento>=21 and mes_de_nacimiento==4) or (dia_de_nacimiento<=21 and mes_de_nacimiento==5):
    print ('Tauro')
if (dia_de_nacimiento>=24 and mes_de_nacimiento==10) or (dia_de_nacimiento<=22 and mes_de_nacimiento==11):
    print ('Escorpio')
if (dia_de_nacimiento>=22 and mes_de_nacimiento==5) or (dia_de_nacimiento<=21 and mes_de_nacimiento==6):
    print ('Geminis')
if (dia_de_nacimiento>=23 and mes_de_nacimiento==11) or (dia_de_nacimiento<=21 and mes_de_nacimiento==12):
    print ('Sagitario')
if (dia_de_nacimiento>=21 and mes_de_nacimiento==6) or (dia_de_nacimiento<=23 and mes_de_nacimiento==7):
    print ('Cancer')
if (dia_de_nacimiento>=22 and mes_de_nacimiento==12) or (dia_de_nacimiento<=20 and mes_de_nacimiento==1):
    print ('Capricornio')
if (dia_de_nacimiento>=24 and mes_de_nacimiento==7) or (dia_de_nacimiento<=23 and mes_de_nacimiento==8):
    print ('Leo')
if (dia_de_nacimiento>=21 and mes_de_nacimiento==1) or (dia_de_nacimiento<=19 and mes_de_nacimiento==2):
    print ('Acuario')
if (dia_de_nacimiento>=24 and mes_de_nacimiento==8) or (dia_de_nacimiento<=23 and mes_de_nacimiento==9):
    print ('Virgo')
if (dia_de_nacimiento>=20 and mes_de_nacimiento==2) or (dia_de_nacimiento<=20 and mes_de_nacimiento==3):
    print ('Piscis')
else : 
    print("no se puede calcular")
