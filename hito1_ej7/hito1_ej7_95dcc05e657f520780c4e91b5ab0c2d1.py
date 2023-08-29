#Zodiaco
#meexeafafdaijfai rgqiugo98wyriguhsiotaouhgsieuhg 
dia=int(input("Ingrese el dia de nacimiento"))
mes=int(input("Ingrese su mes de nacimiento"))
while mes >12:
    mes=int(input("Ingrese su mes de nacimiento"))
while dia> 31:
    dia=int(input("Ingrese el dia de nacimiento"))
signo=""

if mes == 1:
    if dia > 0 and  dia <20 :
        signo = "capricornio"
    elif dia>20:
        signo = "Acuario" 
if mes == 2:
    if dia > 0 and  dia <19 :
        signo = "Acuario"
    elif dia>20:
        signo = "Piscis"
if mes == 3:
    if dia > 0 and  dia <20 :
        signo = "Piscis"
    elif dia>20:
        signo ="Aries"  
if mes == 4:
    if dia > 0 and  dia <19 :
        signo = "Aries"
    elif dia>20:
        signo = "Tauro"
if mes == 5:
    if dia > 0 and  dia <19 :
        signo = "Tauro"
    elif dia>20:
        signo = "Geminis"
if mes == 6:
    if dia > 0 and  dia <19 :
        signo = "Geminis"
    elif dia>20:
        signo = "Cancer"
if mes == 7:
    if dia > 0 and  dia <19 :
        signo = "Cancer"
    elif dia>20:
        signo = "Leo"
if mes == 8:
    if dia > 0 and  dia <19 :
        signo = "Leo"
    elif dia>20:
        signo = "Virgo"
if mes == 9:
    if dia > 0 and  dia <1 :
        signo = "Virgo"
    elif dia>20:
        signo = "Libra"
if mes == 10:
    if dia > 0 and  dia <23 :
        signo = "Libra"
    elif dia>22:
        signo = "Escorpion"
if mes == 11:
    if dia > 0 and  dia <23 :
        signo = "Escorpion"
    elif dia>22:
        signo = "Sagitario"
if mes == 12:
    if dia > 0 and  dia <22 :
        signo = "Sagitario"
    elif dia>21:
        signo = "Capricornio"
print(signo)      