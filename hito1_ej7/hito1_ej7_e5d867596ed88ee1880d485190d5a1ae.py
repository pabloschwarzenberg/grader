#ENTRADA
dia_nac=int(input("ingrese el dia :"))
mes_nac=int(input("ingrese el mes :"))

signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22)

mes_nac=mes_nac-1
if dia_nac >fechas[mes_nac]:
    mes_nac=mes_nac +1
if mes_nac ==12:
    mes_nac =0

print ("Tu signo zodiacal es= " + signo[mes_nac])
