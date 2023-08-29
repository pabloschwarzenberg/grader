#Zodiaco
day=int(input("ingrese dia"))
month=int(input("ingrese fecha(que sea en numero)"))
if (day >=22 or day <=20) and (month==1 or month==12):
        Zodiacos='Capricornio'
        print(Zodiacos)
elif (day >=21 or day <=18) and (month==1 or month==2):
        Zodiacos='Acuario'
        print(Zodiacos)
elif (day >=19 or day <=20) and (month==2 or month==3):
        Zodiacos='Piscis'
        print(Zodiacos)
elif (day >=21 or day <=20) and (month==3 or month==4):
        Zodiacos='Aries'
        print (Zodiacos)
elif (day >=21 or day <=21) and (month==4 or month==5):
        Zodiacos='Tauro'
        print (Zodiacos)
elif (day >=22 or day <=21) and (month==5 or month==6):
        Zodiacos='Geminis'
        print (Zodiacos)
elif (day >22 or day <=22) and (month==6 or month==7):
        Zodiacos='Cancer'
        print (Zodiacos)
elif (day >23 or day <=23) and (month==7 or month==8):
        Zodiacos='Leo'
        print (Zodiacos)
elif (day >24 or day <=23) and (month==8 or month==9):
        Zodiacos='Virgo'
        print(Zodiacos)
elif (day >24 or day <=23) and (month==9 or month==10):
        Zodiacos='Libra'
        print (Zodiacos)
elif (day >24 or day <=22) and (month==10 or month==11):
        Zodiacos='Escorpio'
        print(Zodiacos)
elif (day >23 or day <=21) and (month==11 or month==12):
        Zodiacos='Sagitario'
        print(Zodiacos)
else:
 print("error")