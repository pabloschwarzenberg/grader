#Zodiaco
signos_del_zodiaco = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas_del_zodiaco = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia_de_cumpleanos=int(input("dia de cumpleaños:"))
mes_de_cumpleanos =int(input("mes de cumpleaños:"))

mes_de_cumpleanos = mes_de_cumpleanos -1
if dia_de_cumpleanos>fechas_del_zodiaco[mes_de_cumpleanos]:
    mes_de_cumpleanos = mes_de_cumpleanos +1
if mes_de_cumpleanos == 12:
    mes_de_cumpleanos = 0

print ("Tu signo del zodiaco es: " + signos_del_zodiaco[mes_de_cumpleanos])      