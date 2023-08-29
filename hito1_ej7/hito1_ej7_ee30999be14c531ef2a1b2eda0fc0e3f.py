def signoZodiaco(dia,mes):
  if (21<=dia<=31 and mes==3) or (1<=dia<=20 and mes==4):
    return "Aries"
  elif (20<dia<=31 and mes==4) or (1<=dia<=21 and mes==5):
    return "tauro"
  elif (21<dia<=31 and mes==5) or (1<=dia<=21 and mes==6):
    return "Gemini"
  elif (21<dia<=31 and mes==6) or (1<=dia<=23 and mes==7):
    return "Cancer"
  elif (23<dia<=31 and mes==7) or (1<=dia<=23 and mes==8):
    return "Leo"
  elif (23<dia<=31 and mes==8) or (1<=dia<=23 and mes==9):
    return "Virgo"
  elif (23<dia<=31 and mes==9) or (1<=dia<=23 and mes==10):
    return "Libra"
  elif (23<dia<=31 and mes==10) or (1<=dia<=22 and mes==11):
    return "escorpio"
  elif (22<dia<=31 and mes==11) or (1<=dia<=22 and mes==12):
    return "sagitario"
  elif (22<dia<=31 and mes==12) or (1<=dia<=20 and mes==1):
    return "capricornio"
  elif (20<dia<=31 and mes==1) or (1<=dia<=29 and mes==2):
    return "acuario"
  elif (19<dia<=31 and mes==2) or (1<=dia<21 and mes==3):
    return "piscis"
diaCum=int(input())
mesCum=int(input())
signo=signoZodiaco(diaCum,mesCum)
print(signo)