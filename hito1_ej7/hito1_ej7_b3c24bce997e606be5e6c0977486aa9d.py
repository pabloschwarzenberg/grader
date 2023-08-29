#Zodiaco
signos = ( "Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio","Sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
mes=mes-1
if dia > fechas[mes]:
    mes=mes+1
if mes==12:
    mes=0
print("Su signo zodiacal es", signos[mes])