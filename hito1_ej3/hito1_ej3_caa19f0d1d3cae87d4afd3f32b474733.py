#Aprobación de créditos
def Evaluar_credito():
  Ingreso_en_pesos = float(input("Ingrese si ingreso mensual en pesos:"))
  Ano_de_nacimiento = int(input("Ingrese su ano de nacimiento:"))
  Numero_de_hijos = int(input("Ingrese el numero de hijos:"))
  Anos_de_pertenencia_al_banco = int(input("Ingrese la cantidad de anos de pertenencia al banco:"))
  Estado_civil = input("Ingrese su estado civil (S:soltero, C:casado):")
  Tipo_de_vivienda = input("Ingrese el tipo de vivienda (U:urbano, R:rural):")
  
  if Anos_de_pertenencia_al_banco > 10 and Numero_de_hijos >= 2:
    return "APROBADO"
  elif Estado_civil == "C" and Numero_de_hijos > 3 and 45 <= (2023 - Ano_de_nacimiento) <= 55:
    return "APROBADO"
  elif Ingreso_en_pesos > 2500000 and Estado_civil == "S" and Tipo_de_vivienda == "U":
    return "APROBADO"
  elif Ingreso_en_pesos > 3500000 and Anos_de_pertenencia_al_banco > 5:
    return "APROBADO"
  elif  Tipo_de_vivienda == "R" and Estado_civil == "C" and Numero_de_hijos < 2:
    return "APROBADO"
  else:
    return "RECHAZADO"
    
resultado = Evaluar_credito()
print("El credito es:", resultado)