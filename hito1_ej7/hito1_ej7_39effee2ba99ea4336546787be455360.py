dia = int(input("Ingresa día de nacimiento:\n "))
mes =int(input("Ingresa mes de nacimiento:\n"))
if mes==1:
    signo="Capricornio" if(dia<20) else "Acuario"
if mes==2:
    signo="Acuario" if(dia<19) else "Piscis"
if mes==3:
    signo="Piscis" if(dia<21) else "Aries"
if mes==4:
    signo="Aries" if(dia<20) else "Tauro"
if mes==5:
    signo="Tauro" if(dia<21) else "Geminis"
if mes==6:
    signo="Geminis" if(dia<21) else "Cancer"
if mes==7:
    signo="Cancer" if(dia<23) else "Leo"
if mes==8:
    signo="Leo" if(dia<23) else "Virgo"
if mes==9:
    signo="Virgo" if(dia<23) else "Libra"
if mes==10:
    signo="Libra" if(dia<23) else "Escorpion"
if mes==11:
    signo="Escorpion" if(dia<22) else "Sagitario"
if mes==12:
    signo="Sagitario" if(dia<22) else "Capricornio"

print("Tu signo es:",signo)