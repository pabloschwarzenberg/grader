#Zodiaco
signo =["Capricornio", "Acuario","piscis","Aries","Tauro","Gemenis","cancer","Leo","Virgo","Libra","Scorpion","Sagitario"]
fecha =[20,19,20,21,21,22,22,22,22,22,21]
#ingresa dia de nacimiento
dia =int(input("ingrese dia de nacimiento: "))
while (dia<=1 and dia>=31):
    dia=int(input("error de ingreso de dia"))
    
#ingreso de mes de nacimiento    
mes =int(input("ingrese mes de nacimiento: "))
while (mes<=1 and mes>=12):
    mes=int(input("error de ingreso de mes"))

mes= mes-1

if dia > fecha[mes]:
    mes = mes + 1
if mes ==12:
    mes = 0
    
print("su signo zodiacal es", signo[mes])      