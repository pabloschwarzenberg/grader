#Determine el Signo Zodiacal en base a su fecha de nacimiento

dia=int(input("ingrese su dia de nacimiento "))
mes = int(input("ingrese el número equivalente a su mes de nacimiento "))

#Procedimiento.

if dia >=21 and mes == 3 or  dia <= 20 and mes==4:
    print("Tu signo Zodiacal es Aries")
    
elif dia >= 20 and mes == 4  or dia <= 21  and mes == 5:
    print("Tu signo Zodiacal es Tauro")

elif dia >= 21 and mes == 5 or dia <= 21 and mes==6:
    print("Tu signo Zodiacal es Geminis")

elif dia >= 21 and mes == 6 or dia <= 23 and mes == 7:
    print("Tu signo Zodiacal es Cáncer")

elif dia >= 23 and mes == 7 or dia <= 23 and mes == 8:
    print("Tu signo Zodiacal es Leo")

elif dia >= 23 and mes == 8 or dia <= 23 and mes == 9:
    print("Tu signo Zodiacal es Virgo")

elif dia >= 23 and mes == 9 or dia <= 23 and mes == 10:
    print("Tu signo Zodiacal es Libra")
elif dia >= 23 and mes == 10 or dia <= 22 and mes == 11:
    print("Tu signo Zodiacal es Escorpión")

elif dia >= 23 and mes == 11 or dia <= 22 and mes == 12:
    print("Tu signo Zodiacal es Sagitario")

elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
    print("Tu signo Zodiacal es Capricornio")

elif dia >=20 and mes == 1 or dia <=19 and mes ==2 :
    print ("Tu signo Zodiacal es Acuario")

elif dia >= 19 and mes ==2 or mes==3 and dia <=21 :
    print("Tu signo Zodiacal es Picis")
else:
    print("Dato invalido , intentelo nuevamente.")