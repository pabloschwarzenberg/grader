dia = int()
mes = int()
signo = str()

print ("Ingrese el valor de dia:")
dia =  int(input())
print ("Ingrese el valor de mes:")
mes =  int(input())

if (dia>=21 and mes==3) or (dia<=20 and mes==4):
  signo = "Aries"
if (dia>=24 and mes==9) or (dia<=23 and mes==10):
  signo = "Libra"
if (dia>=21 and mes==4) or (dia<=21 and mes==5):
  signo = "Tauro"
if (dia>=24 and mes==10) or (dia<=22 and mes==11):
  signo = "Escorpio"
if (dia>=22 and mes==5) or (dia<=21 and mes==6):
  signo = "Geminis"
if (dia>=23 and mes==11) or (dia<=21 and mes==12):
  signo = "sagitario"
if (dia>=21 and mes==6) or (dia<=23 and mes==7):
  signo = "cancer"
if (dia>=22 and mes==12) or (dia<=20 and mes==1):
  signo = "capricornio"
if (dia>=24 and mes==7) or (dia<=23 and mes==8):
  signo = "leo"
if (dia>=21 and mes==1) or (dia<=19 and mes==2):
  signo = "acuario"
if (dia>=24 and mes==8) or (dia<=23 and mes==9):
  signo = "virgo"
if (dia>=20 and mes==2) or (dia<=20 and mes==3):
  signo = "piscis"

print (signo)
