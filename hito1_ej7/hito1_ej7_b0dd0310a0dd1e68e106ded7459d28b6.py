#Zodiaco
dia=int(input("Ingrese día de nacimiento: "))
while dia<=0:
    print("Escriba correctamente el día, vuelva a intentarlo")
    dia=int(input("Ingrese día de nacimiento: "))
while dia>32:
    print("Escriba correctamente el día, vuelva a intentarlo")
    dia=int(input("Ingrese día de nacimiento: "))
if 0<dia<32:
    mes=int(input("Ingrese mes de nacimiento: "))
while mes<=0:
    print("Escriba correctamente el mes, vuelva a intentarlo")
    mes=int(input("Ingrese mes de nacimiento: "))
while mes>12:
    print("Escriba correctamente el mes, vuelva a intentarlo")
    mes=int(input("Ingrese mes de nacimiento: "))
if 0<mes<13:
    print("espere un momento por favor")
m= mes*100
resultado=m+dia
if 321<=resultado<=420:
    print("Tu signo zodiacal es Aries")
elif 421<=resultado<=521:
    print("Tu signo zodiacal es Tauro")
elif 522<=resultado<=621:
    print("Tu signo zodiacal es Géminis") 
elif 622<=resultado<=722:
    print("Tu signo zodiacal es Cáncer")
elif 723<=resultado<=822:
    print("Tu signo zodiacal es Leo")
elif 823<=resultado<=923:
    print("Tu signo zodiacal es Virgo") 
elif 924<=resultado<=1023:
    print("Tu signo zodiacal es Libra")
elif 1024<=resultado<=1122:
    print("Tu signo zodiacal es Escorpio") 
elif 1123<=resultado<=1221:
    print("Tu signo zodiacal es Sagitario")
elif 1222<=resultado<=120:
    print("Tu signo zodiacal es Capricornio")
elif 121<=resultado<=219:
    print("Tu signo zodiacal es Acuario") 
elif 220<=resultado<=320:
    print("Tu signo zodiacal es Piscis")
else:
    print("Usted no tiene signo zodiacal")      