#Aprobación de créditos
TempA = int(input(""))  # Ingreso
TempB = int(input(""))  # Año de nacimiento
TempC = int(input(""))  # Número de hijos
TempD = int(input(""))  # Años de pertenencia al banco
TempE = input("")  # Estado civil
TempF = input("")  # Urbano, rural

if (TempD > 10 and TempC >= 2) or (TempE == "C" and TempC > 3 and 45 <= 2017 - TempB <= 55) or (TempA > 2500000 and TempE == "S" and TempF == "U") or (TempA > 3500000 and TempD > 5) or (TempF == "R" and TempE == "C" and TempC < 2):
  print("APROBADO")
else:
  print("RECHAZADO")
