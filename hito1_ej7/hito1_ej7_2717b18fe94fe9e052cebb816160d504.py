#Zodiaco
      
d=int(input("Dia de nacimiento: "))
m=int(input("Mes de nacimiento: "))

if(m == 1):
	if(d < 20):
		print("Capricornio")
	else:
		print("Acuario")

elif(m == 2):
	if(d < 19):
		print("Acuario")
	else:
		print("Piscis")

elif(m == 3):
	if(d < 21):
		print("Piscis")
	else:
		print("Aries")

elif(m == 4):
	if(d < 20):
		print("Aries")
	else:
		print("Tauro")

elif(m == 5):
	if(d < 20):
		print("Tauro")
	else:
		print("Géminis")

elif(m == 6):
	if(d < 21):
		print("Géminis")
	else:
		print("Cáncer")

elif(m == 7):
	if(d < 23):
		print("Cáncer")
	else:
		print("Leo")

elif(m == 8):
	if(d < 23):
		print("Leo")
	else:
		print("Virgo")

elif(m == 9):
	if(d < 23):
		print("Virgo")
	else:
		print("Libra")

elif(m == 10):
	if(d < 23):
		print("Libra")
	else:
		print("Escorpio")

elif(m == 11):
	if(d < 22):
		print("Escorpio")
	else:
		print("Sagitario")

elif(m == 12):
	if(d < 22):
		print("Sagitario")
	else:
		print("Capricornio")