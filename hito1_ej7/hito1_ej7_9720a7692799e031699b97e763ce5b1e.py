#Zodiaco
dia = int(input("Ingrese su dia de nacimiento:"))  
mes = int(input("Ingrese su mes de nacimiento:"))
if mes == int("03") and dia >= int("21") or mes == int("04") and dia <= int("20"):
  print("Su signo es Aries")
elif mes == int("04") and dia >= int("20") or mes == int("05") and dia <= int("21"):
  print("Su signo es Tauro")
elif mes == int("05") and dia >= int("21") or mes == int("06") and dia <= int("21"):
  print("Su signo es Geminis")
elif mes == int("06") and dia >= int("21") or mes == int("07") and dia <= int("23"):
  print("Su signo es Cancer")
elif mes == int("07") and dia >= int("23") or mes == int("08") and dia <= int("23"):
  print("Su signo es Leo")
elif mes == int("08") and dia >= int("23") or mes == int("09") and dia <= int("23"):
  print("Su signo es Virgo")
elif mes == int("09") and dia >= int("23") or mes == int("10") and dia <= int("23"):
  print("Su signo es Libra")
elif mes == int("10") and dia >= int("23") or mes == int("11") and dia <= int("22"):
  print("Su signo es Escorpio")
elif mes == int("11") and dia >= int("22") or mes == int("12") and dia <= int("22"):
  print("Su signo es Sagitario")
elif mes == int("12") and dia >= int("22") or mes == int("01") and dia <= int("20"):
  print("Su signo es Capricornio")
elif mes == int("01") and dia >= int("20") or mes == int("02") and dia <= int("19"):
  print("Su signo es Acuario")
elif mes == int("10") and dia >= int("19") or mes == int("11") and dia <= int("21"):
  print("Su signo es Piscis")