#Zodiaco
signo = ["capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario"]
fecha= [20, 19, 20, 20, 21, 21, 22, 22, 23, 23, 22, 21]

dia=int(input("Ingrese el dia:"))
mes= int(input("Ingrese el mes:"))

mes= mes - 1
if dia>fecha[mes]:
    mes= mes + 1
if mes == 12:
    mes = 0

print("Signo:", signo[mes])
