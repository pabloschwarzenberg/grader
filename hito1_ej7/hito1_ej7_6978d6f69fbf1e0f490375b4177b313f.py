S = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
F = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

D=int(input("Ingrese el día de su cumpleaños :"))
M=int(input("Ingrese el mes en que nació :"))

M=M-1
if D>F[M]:
    M=M+1
if M==12:
    M=0

print ("Tu signo zodiacal es: " + S[M])