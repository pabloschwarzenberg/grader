dia=int(input())
mes=int(input())
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", " geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
mes=mes-1
if dia>fechas[mes]:
    mes=mes+1
if mes==12:
    mes=0
print("tu signo es: "+ signo[mes])