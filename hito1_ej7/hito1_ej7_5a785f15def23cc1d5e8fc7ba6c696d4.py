#Zodiaco
signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpion", "Sagitario"]

dia = int(input("Dia de nacimiento:"))
mes = int(input("Mes de nacimiento:"))

if mes == 1 and dia >= 20 or mes == 2 and dia < 19:
 print(signo[1])
elif mes == 2 and dia >= 19 or mes == 3 and dia < 21:
 print(signo[2])
elif mes == 3 and dia >= 21 or mes == 4 and dia < 20:
 print(signo[3])
elif mes == 4 and dia >= 20 or mes == 5 and dia < 21:
 print(signo[4])
elif mes == 5 and dia >= 21 or mes == 6 and dia < 21:
 print(signo[5])
elif mes == 6 and dia >= 21 or mes == 7 and dia < 23:
 print(signo[6])
elif mes == 7 and dia >= 23 or mes == 8 and dia < 23:
 print(signo[7])
elif mes == 8 and dia >= 23 or mes == 9 and dia < 23:
 print(signo[8])
elif mes == 9 and dia >= 23 or mes == 10 and dia < 23:
 print(signo[9])
elif mes == 10 and dia >= 23 or mes == 11 and dia < 22:
 print(signo[10])
elif mes == 11 and dia >= 22 or mes == 12 and dia < 21:
 print(signo[11])
elif mes == 12 and dia >= 22 or mes == 1 and dia < 20:
 print(signo[0])