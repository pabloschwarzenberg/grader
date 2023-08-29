#Zodiaco
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (13, 19, 20, 9, 15, 30, 22, 29, 17, 18, 15, 11, 18)

dia = int(input("dia :"))
mes = int(input("mes :"))

mes = mes-1
if dia > fechas [mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print("Tu signo es: " + signo [mes])

if ((mes==4) and (dia>=19)) or ((mes==5) and (dia<=13)):
    signo = 'Aries'

if ((mes==5) and (dia>=14)) or ((mes==6) and (dia<=19)):
    signo = 'Tauro'

if ((mes==6) and (dia>=20)) or ((mes==7) and (dia<=20)):
    signo = 'Gemenis'

if ((mes==7) and (dia>=21)) or ((mes==8) and (dia<=9)):
    signo = 'Cancer'

if ((mes==8) and (dia>=10)) or ((mes==9) and (dia<=15)):
    signo = 'Leo'

if ((mes==9) and (dia>=16)) or ((mes==10) and (dia<=30)):
    signo = 'Virgo'

if ((mes==10) and (dia>=31)) or ((mes==11) and (dia<=22)):
    signo = 'Libra'

if ((mes==11) and (dia>=23)) or ((mes==11) and (dia<=29)):
    signo = 'Escorpion'

if ((mes==11) and (dia>=30)) or ((mes==12) and (dia<=17)):
    signo = 'Ophiuchus'

if ((mes==12) and (dia>=18)) or ((mes==1) and (dia<=18)):
    signo = 'Sagitario'

if ((mes==1) and (dia>=19)) or ((mes==2) and (dia<=15)):
    signo = 'Capricornio'

if ((mes==2) and (dia>=16)) or ((mes==3) and (dia<=11)):
    signo = 'Acuario'

if ((mes==3) and (dia>=12)) or ((mes==4) and (dia<=18)):
    signo = 'Picis'