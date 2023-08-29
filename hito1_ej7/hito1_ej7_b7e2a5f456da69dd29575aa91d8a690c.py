#Zodiaco
#Lista de signos del zodiaco y las fechas correspondientes a estas
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
#Pide al usuario dia y mes de cumpleaños
dia = int(input("Ingrese día de cumpleaños :"))
mes = int(input("Ingrese mes de cumpleaños :"))

mes = mes-1
if dia > fechas[mes]:
    mes = mes+1
if mes == 12:
    mes = 0

print ("Tu signo es: " + signo[mes])