#Zodiaco
dia=int(input("ingrese el dia de su cumpleaños: "))
mes=int(input("ingrese el mes de su cumpleaños: "))

#aries
if ((dia>=21 and mes==3) or (dia<=20 and mes==4)):
  print("usted pertenece a aries")
  
elif ((dia>=20 and mes==4) or (dia<=21 and mes==5)):
  print("usted pertenece a tauro")
  
elif ((dia>=21 and mes==5) or (dia<=21 and mes==6)):
  print("usted pertenece a geminis")
  
elif ((dia>=21 and mes==6) or (dia<=23 and mes==7)):
  print("usted pertenece a cancer")

elif ((dia>=23 and mes==7) or (dia<=22 and mes==8)):
  print("usted pertenece a leo")
  
elif ((dia>=23 and mes==8) or (dia<=22 and mes==9)):
  print("usted pertenece a virgo")
  
elif ((dia>=23 and mes==9) or (dia<=22 and mes==10)):
  print("usted pertenece a libra")
 
elif ((dia>=23 and mes==10) or (dia<=22 and mes==11)):
  print("usted pertenece a escorpio")
  
elif ((dia>=23 and mes==11) or (dia<=21 and mes==12)):
  print("usted pertenece a sagitario")
  
elif ((dia>=22 and mes==12) or (dia<=20 and mes==1)):
  print("usted pertenece a capricornio")
  
elif ((dia>=19 and mes==1) or (dia<=19 and mes==2)):
  print("usted pertenece a acuario")
  
elif ((dia>=20 and mes==2) or (dia<=20 and mes==3)):
  print("usted pertenece a piscis")