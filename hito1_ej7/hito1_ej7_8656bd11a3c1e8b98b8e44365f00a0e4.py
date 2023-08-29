#Zodiaco
dia=int(input("dia :"))
mes=int(input("mes :"))

if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)):
    signo = 'aries'
if ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=21)):
    signo = 'Tauro'
if ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)):
    signo = 'Geminis'
if ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=23)):
    signo = 'Cáncer'
if ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):
    signo = 'Leo'
if ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=23)):
    signo = 'Virgo'
if ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=23)):
    signo = 'Libra'
if ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=22)):
    signo = 'Escorpion'
if ((mes==11) and (dia>=23)) or ((mes==12) and (dia<=22)):
    signo = 'Sagitario'
if ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
    signo = 'Capricornio'
if ((mes==1) and (dia>=20)) or ((mes==2) and (dia<=19)):
    signo = 'Acuario'
if ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=21)):
    signo = 'Piscis'

print ("Tu signo es: " + signo)     