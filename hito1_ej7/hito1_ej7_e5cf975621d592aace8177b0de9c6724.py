#Zodiaco
dia=eval(input("dia:"))
mes=eval(input("mes:"))

if mes == 1:
  mes = 'enero'
elif mes == 2:
  mes = 'febrero'
elif mes == 3:
  mes = 'marzo'
elif mes == 4:
  mes = 'abril'
elif mes == 5:
  mes = 'mayo'
elif mes == 6:
  mes = 'junio'
elif mes == 7:
  mes = 'julio'
elif mes == 8:
  mes = 'agosto'
elif mes == 9:
  mes = 'septiembre'
elif mes == 10:
  mes = 'octubre'
elif mes == 11:
  mes = 'noviembre'
else:
  mes = 'dicembre'

if dia >= 21 and mes =='marzo' or dia < 20 and mes =='abril':
  print("aries")
elif dia >= 20 and mes =='abril' or dia < 21 and mes =='mayo':
  print("tauro")
elif dia >= 21 and mes =='mayo' or dia < 21 and mes =='junio':
  print("geminis")
elif dia >= 21 and mes =='junio' or dia < 23 and mes =='julio':
  print("cancer")
elif dia >= 23 and mes =='julio' or dia < 23 and mes =='agosto':
  print("leo")
elif dia >= 23 and mes =='agosto' or dia < 23 and mes =='septiembre':
  print("virgo")
elif dia >= 23 and mes =='septiembre' or dia < 23 and mes =='octubre':
  print("libra")
elif dia >= 23 and mes =='octubre' or dia < 22 and mes =='noviembre':
  print("escorpio")
elif dia >= 22 and mes =='noviembre' or dia < 22 and mes =='diciembre':
  print("sagitario")
elif dia >= 22 and mes =='diciembre' or dia < 20 and mes =='enero':
  print("capricornio")
elif dia >= 20 and mes =='enero' or dia < 19 and mes =='febrero':
  print("acuario")
else:
  print("piscis")