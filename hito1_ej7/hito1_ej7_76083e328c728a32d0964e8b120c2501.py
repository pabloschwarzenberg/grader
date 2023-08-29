#Zodiaco
dia=eval(input("ingrese el dia de nacimiento"))
mes=eval(input("ingrese el mes de nacimiento"))

if mes == 1:
  mes = "enero"
elif mes ==2:
  mes = "febrero"
elif mes ==3:
  mes = "marzo"
elif mes ==4:
  mes = "abril"
elif mes ==5:
  mes = "mayo"
elif mes ==6:
  mes = "junio"
elif mes ==7:
  mes = "julio"
elif mes ==8:
  mes = "agosto"
elif mes ==9:
  mes = "septiembre"
elif mes ==10:
  mes = "octubre"
elif mes ==11:
  mes = "noviembre"
else:
  mes = "dicembre"

if dia >= 21 and mes =="marzo" or dia>=1 and dia<20 and mes=="abril":
  print("Aries")
elif dia >= 20 and mes =="abril" or dia>=1 and dia<21 and mes=="mayo":
  print("Tauro")
elif dia >= 21 and mes =="mayo" or dia>=1 and dia<21 and mes=="junio":
  print("Geminis")
elif dia >= 21 and mes =="junio" or dia>=1 and dia<23 and mes=="julio":
  print("Cancer")  
elif dia >= 23 and mes =="julio" or dia>=1 and dia<23 and mes=="agosto":
  print("Leo")
elif dia >= 23and mes =="agosto" or dia>=1 and dia<23 and mes=="septiembre":
  print("Virgo")
elif dia >= 23 and mes =="septiembre" or dia>=1 and dia<23 and mes=="octubre":
  print("Libra")
elif dia >= 23 and mes =="octubre" or dia>=1 and dia<22 and mes=="noviembre":
  print("Escorpion")
elif dia >= 22 and mes =="noviembre" or dia>=1 and dia<22 and mes=="diciembre":
  print("Sagitario")
elif dia >= 22 and mes =="diciembre" or dia>=1 and dia<20 and mes=="enero":
  print("Capricornio")
elif dia >= 20 and mes =="enero" or dia>=1 and dia<19 and mes=="febrero":
  print("Acuario")
else:
    print("Piscis")    