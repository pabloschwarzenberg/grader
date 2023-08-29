#Zodiaco
signo = ["Capricornio","Acuario","Piscis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpio","Sagitario"]
fecha = [20,19,20,21,21,22,22,22,22,22,21]

mes = [0,12]
dia = int(input("Ingrese día de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))

mes = mes-1
if dia > fecha[mes]:
    mes = mes+1

if mes == 12:
    mes = 0

print("Su signo zodiacal es: ", signo[mes])