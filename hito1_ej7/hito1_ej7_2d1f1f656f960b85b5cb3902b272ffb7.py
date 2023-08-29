#Zodiaco
Z=["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
T=[20, 19, 20, 21, 21, 22, 22, 22, 22, 22, 21]
M = int(input("mes de nacimineto:"))
D = int(input("dia de nacimiento:"))
M=M-1
if D > T[M]:
    M=M+1
if M == 12:
    M=0
print("Signo zodiacal:", Z[M])