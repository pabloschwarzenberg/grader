#Zodiaco
dia=eval(input('Ingrese dia: '))
mes=eval(input('Ingrese mes: '))
if (dia>=21 and dia<=31 and mes==3) or (dia>=1 and dia<=19 and mes==4):
  signo='Aries'
if (dia>=20 and dia<=30 and mes==4) or (dia>=1 and dia<=20 and mes==5):
  signo='Tauro'
if (dia>=21 and dia<=31 and mes==5) or (dia>=1 and dia<=20 and mes==6):
  signo='Geminis'
if (dia>=21 and dia<=30 and mes==6) or (dia>=1 and dia<=22 and mes==7):
  signo='Cancer'
if (dia>=23 and dia<=31 and mes==7) or (dia>=1 and dia<=22 and mes==8):
  signo='Leo'
if (dia>=23 and dia<=31 and mes==8) or (dia>=1 and dia<=22 and mes==9):
  signo='Virgo'
if (dia>=23 and dia<=30 and mes==9) or (dia>=1 and dia<=22 and mes==10):
  signo='Libra'
if (dia>=23 and dia<=31 and mes==10) or (dia>=1 and dia<=21 and mes==11):
  signo='Scorpio'
if (dia>=22 and dia<=30 and mes==11) or (dia>=1 and dia<=21 and mes==12):
  signo='Sagitario'
if (dia>=22 and dia<=31 and mes==12) or (dia>=1 and dia<=19 and mes==1):
  signo='Capricornio'
if (dia>=20 and dia<=31 and mes==1) or (dia>=1 and dia<=18 and mes==2):
  signo='Acuario'
if (dia>=19 and dia<=29 and mes==2) or (dia>=1 and dia<=20 and mes==3):
  signo='Piscis'
print(signo)