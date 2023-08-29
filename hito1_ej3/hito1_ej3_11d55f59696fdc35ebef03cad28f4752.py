Ingreso = eval(input())
year = eval(input())
hijo = eval(input())
anti = eval(input())
civil = input()
terreno = input()
if anti >= 10 and hijo >= 2:
  print("APROBADO")
elif civil == "C" and hijo >= 3 and year >= 45 and year <= 55:
  print("APROBADO")
elif Ingreso >= 2500000 and civil == "S" and terreno == "U":
  print("APROBADO")
elif Ingreso >= 3500000 and anti > 5:
  print("APROBADO")
elif terreno == "R" and civil == "C" and hijo < 2:
  print("APROBADO")
else:
  print("RECHAZADO")