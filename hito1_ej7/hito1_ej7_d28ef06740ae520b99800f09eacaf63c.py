#Zodiaco
dia=int(input("Ingrese dia de cumpleaños"))
mes=int(input("Ingrese mes de cumpleaños"))

if mes==1:
  if 21<=dia<=30:
    print ("ACUARIO")
  else:
    print ("CAPRICORNIO")
elif mes==2:
  if 20<=dia<=29:
    print ("PISCIS")
  else:
    print ("ACUARIO")
elif mes==3:
  if 21<=dia<=30:
    print ("ARIES")
  else:
    print ("PISCIS")
elif mes==4:
  if 21<=dia<=30:
    print ("TAURO")
  else:
    print ("ARIES")
elif mes==5:
  if 22<=dia<=30:
    print ("GEMINIS")
  else:
    print ("TAURO")
elif mes==6:
  if 22<=dia<=30:
    print ("CANCER")
  else:
    print ("GEMINIS")
elif mes==7:
  if 23<=dia<=30:
    print ("LEO")
  else:
    print ("CANCER")
elif mes==8:
  if 23<=dia<=30:
    print ("VIRGO")
  else:
    print ("LEO")
elif mes==9:
  if 24<=dia<=30:
    print ("LIBRA")
  else:
    print ("VIRGO")
elif mes==10:
  if 24<=dia<=30:
    print ("ESCORPION")
  else:
    print ("LIBRA")
elif mes==11:
  if 23<=dia<=30:
    print ("SAGITARIO")
  else:
    print ("ESCORPION")
elif mes==12:
  if 22<=dia<=31:
    print ("CAPRICORNIO")
  else:
    print ("SAGITARIO")