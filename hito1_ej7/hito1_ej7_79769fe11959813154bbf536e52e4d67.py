#Zodiaco
signo_zodiacal =["Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]
z = int(input("ingresa un numero :"))
if(z>=1 and z<=12):
    print("signo_zodiacal" + str(z) + " es: " + signo_zodiacal[z-1])
else:
    print("no existe ese signo zodiacal")
