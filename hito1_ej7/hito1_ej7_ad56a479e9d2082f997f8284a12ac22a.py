dia = int (input ("Ingresa dia de nacimiento: "))
mes = int (input ("Ingresa mes de nacimiento: "))
if(dia>=21 and dia<32 and mes==3) or (dia<=20 and mes==4):
    print ("Por desgracia eres Aries")
elif(dia>=24 and mes==9) or (dia<=23 and mes==10):
    print ("Eres Libra aceptable")
elif(dia>=20 and dia<32 and mes==4) or (dia<=21 and mes==5):
    print ("Manito eres Tauro vuelve a nacer")
elif(dia>=24 and mes==10) or (dia<=22 and mes==11):
    print ("Eres Escorpio podria ser mejor")
elif(dia>=22 and mes==5) or (dia<=21 and mes==6):
    print ("Eres geminis aceptable")
elif(dia>=23 and mes==11) or (dia<=21 and mes==12):
    print ("Por desgracia eres Sagitario")
elif(dia>=21 and mes==6) or (dia<=23 and mes==7):
    print ("Manito eres Cancer")
elif(dia>=22 and mes==12) or (dia<=20 and mes==1):
    print ("Eres Capricornio ninguna queja")
elif(dia>=23 and mes==7) or (dia<=23 and mes==8):
    print ("Buena eres Leo best signo")
elif(dia>=21 and mes==1) or (dia<=19 and mes==2):
    print ("Ok, eres Acuario ahora en serio vuelve a nacer")
elif(dia>=24 and mes==8) or (dia<=23 and mes==9):
    print ('Virgo')
elif(dia>=20 and mes==2) or (dia<=20 and mes==3):
    print ('Piscis')
print ()