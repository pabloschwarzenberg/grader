#Zodiaco
def zodiaco(day,month):
    if (day >=21 or day <=20) and (month==3 or month==4):
        Zodiacos='Aries'
        return Zodiacos
    elif (day >=21 or day <=21) and (month==4 or month==5):
        Zodiacos='Tauro'
        return Zodiacos
    elif (day >=22 or day <=22) and (month==6 or month==7):
        Zodiacos='Cancer'
        return Zodiacos
    elif (day >=22 or day <=21) and (month==5 or month==6):
        Zodiacos='Geminis'
        return Zodiacos
    
        
    elif (day >=23 or day <=23) and (month==7 or month==8):
        Zodiacos='Leo'
        return Zodiacos
    elif (day >=24 or day <=23) and (month==8 or month==9):
        Zodiacos='Virgo'
    elif (day >=24 or day <=23) and (month==9 or month==10):
        Zodiacos='Libra'
        return Zodiacos
    elif (day >=24 or day <=22) and (month==10 or month==11):
        Zodiacos='Escorpio'
        return Zodiacos
    elif (day >=21 or day <=18) and (month==1 or month==2):
        Zodiacos='Acuario'
        return Zodiacos
    elif (day >=23 or day <=21) and (month==11 or month==12):
        Zodiacos='Sagitario'
        return Zodiacos
    elif (day >=22 or day <=20) and (month==1 or month==12):
        Zodiacos='Capricornio'
        return Zodiacos
    elif (day >=19 or day <=20) and (month==2 or month==3):
        Zodiacos='Piscis'
        return Zodiacos

dia=int(input('dia de nacimiento'))
mess=int(input('numero de mes de nacimiento'))
zodia=zodiaco(dia,mess)
print(zodia)