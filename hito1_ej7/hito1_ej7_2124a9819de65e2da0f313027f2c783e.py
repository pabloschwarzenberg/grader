#Zodiaco
#Zodiaco
dia = int(input("Ingrese día de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento (N°): "))



if (21 <= dia <= 31) and (mes == 3) or (1 <= dia <= 20) and (mes == 4):
    signo = "Aries"
    
if (21 <= dia <= 30) and (mes == 4) or (1 <= dia <= 21) and (mes == 5):
    signo = "Tauro"
    
if (22 <= dia <= 31) and (mes == 5) or (1 <= dia <= 21) and (mes == 6):    
    signo = "Geminis"
    
if (22 <= dia <= 30) and (mes == 6) or (1 <= dia <= 22) and (mes == 7):    
    signo = "Cancer"
    
if (23 <= dia <= 31) and (mes == 7) or (1 <= dia <= 23) and (mes == 8):    
    signo = "Leo"
    
if (24 <= dia <= 31) and (mes == 8) or (1 <= dia <= 23) and (mes == 9):    
    signo = "Virgo"
    
if (24 <= dia <= 30) and (mes == 9) or (1 <= dia <= 23) and (mes == 10):    
    signo = "Libra"
    
if (24 <= dia <= 31) and (mes == 10) or (1 <= dia <= 22) and (mes == 11):    
    signo = "Escorpion"
    
if (23 <= dia <= 30) and (mes == 11) or (1 <= dia <= 21) and (mes == 12):    
    signo = "Sagitario"
    
if (22 <= dia <= 31) and (mes == 12) or (1 <= dia <= 20) and (mes == 1):    
    signo = "Capricornio"
    
if (21 <= dia <= 31) and (mes == 1) or (1 <= dia <= 19) and (mes == 2):    
    signo = "Aquario"
    
if (20 <= dia <= 29) and (mes == 2) or (1 <= dia <= 20) and (mes == 3):   
    signo = "Piscis"
    

print ("El signo sodiacal es: ", (signo))      