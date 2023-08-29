#Zodiaco
sig_zod = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fecha_nac = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia=int(input("dia de nacimiento :"))
mes=int(input("mes de nacimiento :"))

mes=mes-1
if dia>fecha_nac[mes]:
    mes=mes+1
if mes==12:
    mes=0

print ("Tu signo es: " + sig_zod[mes])   