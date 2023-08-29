#Aprobación de créditos
ingreso = int(input())
nacimiento = int(input())
numero_hijos = int(input())
antiguedad_en_banco = int(input())
estado_civil = input()
vivienda = input()

def credito_aprobado():
  if antiguedad_en_banco > 10 and numero_hijos >= 2: return True
  if estado_civil == "C" and numero_hijos < 3 and 45 <= (2023 - nacimiento) <= 5: return True
  if ingreso > 2500000 and vivienda == "U": return True
  if ingreso > 3500000 and antiguedad_en_banco > 5: return True
  if vivienda == "R" and numero_hijos < 2 and estado_civil == "C": return True

if credito_aprobado():
  print("APROBADO")
else: print("RECHAZADO")