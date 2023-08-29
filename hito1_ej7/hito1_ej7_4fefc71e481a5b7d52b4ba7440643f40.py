#Zodiaco
signo=["Capricornio","Acuario","Cancer","Zagitario","Tauro","Geminis","Aries","Leo","Virgo","Escorpio","Picis","Sagitario"]

fecha=[21,22,21,23,21,22,24,22,21,21,21,22]
#mes=[Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,Diciembre]

#Datos de nacimientos
dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))


mes= mes - 1
if dia > fecha[mes]: 
     mes= mes + 1
if mes== 12:
     mes= 0
print("Su signo zodiacal es ", signo[mes])