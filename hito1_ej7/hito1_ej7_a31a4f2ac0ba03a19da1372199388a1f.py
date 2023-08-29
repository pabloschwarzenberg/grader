#Zodiaco

dia=int(input())
mes=int(input())

if 24<=dia<=31 and mes==3 or mes==4 and 1<=dia<=21:
  print("Aries")
 
elif 22<=dia<=30 and mes==4 or mes==5 and 1<=dia<=21:
  print("Tauro")
  
elif 22<=dia<=31 and mes==5 or mes==6 and 1<=dia<=21:
  print("geminis")
  
elif 20<=dia<=30 and mes==6 or mes==7 and 1<=dia<=21:
  print("Cáncer")
  
elif 22<=dia<=31 and mes==7 or mes==8 and 1<=dia<=22:
  print("Leo")
  
elif 23<=dia<=31 and mes==8 or mes==9 and 1<=dia<=21:
  print("Virgo")
  
elif 22<=dia<=30 and mes==9 or mes==10 and 1<=dia<=21:
  print("Libra")
  
elif 22<=dia<=31 and mes==10 or mes==11 and 1<=dia<=22:
  print("Escorpio")
  
elif 23<=dia<=30 and mes==11 or mes==12 and 1<=dia<=21:
  print("Sagitario")
  
elif 22<=dia<=31 and mes==12 or mes==1 and 1<=dia<=21:
  print("Capricornio")
  
elif 22<=dia<=31 and mes==1 or mes==2 and 1<=dia<=21:
  print("Acuario")
  
elif 22<=dia<=28 and mes==2 or mes==3 and 1<=dia<=23:
  print("Piscis")