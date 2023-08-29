#Zodiaco
dia = int(input("Ingrese dia de Nacimiento: "))
mes = int(input("Ingrese mes de Nacimiento: "))
if(((dia >= 21) and (mes == 3)) or ((dia <= 20) and (mes == 4))):
	zodiaco = 'Aries'
if(((dia >= 20) and (mes == 4)) or ((dia <= 21) and (mes == 5))):
	zodiaco = 'Tauro'
if(((dia >= 21) and (mes == 5)) or ((dia <= 21) and (mes == 6))):
	zodiaco = 'Geminis'
if(((dia >= 21) and (mes == 6)) or ((dia <= 223) and (mes == 7))):
	zodiaco = 'Cancer'
if(((dia >= 23) and (mes == 7)) or ((dia <= 23) and (mes == 8))):
	zodiaco = 'Leo'
if(((dia >= 23) and (mes == 8)) or ((dia <= 23) and (mes == 9))):
	zodiaco = 'Virgo'
if(((dia >= 23) and (mes == 9)) or ((dia <= 23) and (mes == 10))):
	zodiaco = 'Libra'
if(((dia >= 23) and (mes == 10)) or ((dia <= 22) and (mes == 11))):
	zodiaco = 'Scorpion'
if(((dia >= 23) and (mes == 11)) or ((dia <= 22) and (mes == 12))):
	zodiaco = 'Sagitario'
if(((dia >= 22) and (mes == 12)) or ((dia <= 20) and (mes == 1))):
	zodiaco = 'Capricornio'
if(((dia >= 20) and (mes == 1)) or ((dia <= 19) and (mes == 2))):
	zodiaco = 'Acuario'										
if(((dia >= 19) and (mes == 2)) or ((dia <= 21) and (mes == 3))):
	zodiaco = 'Piscis'
print(zodiaco)