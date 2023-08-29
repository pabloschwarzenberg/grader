dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento en numeros del 1 al 12: "))

signo = ""

if mes == 1:
	if dia >= 20:
		signo = "ACUARIO"
	else:
		signo = "CAPRICORNIO"

elif mes == 2:
	if dia >= 19:
		signo  = "PISCIS"
	else:
		signo = "ACUARIO"
		
elif mes == 3:
	if dia >= 21:
		signo = "ARIES"
	else:
		signo = "PISCIS"

elif mes == 4:
			if dia >= 20:
				signo = "TAURO"
			else:
				signo = "ARIES"
				
elif mes == 5:
			if dia >= 21:
				signo = "GEMINIS"
			else:
				signo = "TAURO"
				
elif mes == 6:
			if dia >= 21:
				signo = "CANCER"
			else:
				signo = "GEMINIS"
				
elif mes == 7:
			if dia >= 23:
				signo = "LEO"
			else:
				signo = "CANCER"
				
elif mes == 8:
			if dia >= 23:
				signo = "VIRGO"
			else:
				signo = "LEO"
				
elif mes == 9:
			if dia >= 23:
				signo = "LIBRA"
			else:
				signo = "VIRGO"
				
elif mes == 10:
			if dia >= 23:
				signo = "ESCORPIO"
			else:
				signo = "LIBRA"
				
elif mes == 11:
			if dia >= 23:
				signo = "SAGITARIO"
			else:
				signo = "ESCORPIO"
				
elif mes == 12:
			if dia >= 22:
				signo = "CAPRICORNIO"
			else:
				signo = "SAGITARIO"

print(signo)