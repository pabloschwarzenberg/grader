#Zodiaco
#signo zodiacal
#SIGNO
Signo=["capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo",
      "virgo","libra","scorpio","sagitario"]
Fecha=[20,19,21,20,20,21,21,23,23,23,23,23,22]
D=int(input("Ingrese su dia de nacimiento:"))
M=int(input("Ingrese en numeros su mes de nacimiento:"))
M=M-1
if D>Fecha[M]:
    M=M+1
if M==12:
    M==0
print("",Signo[M],"")