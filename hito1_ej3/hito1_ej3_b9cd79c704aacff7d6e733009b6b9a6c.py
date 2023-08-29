#Aprobación de créditos
ingreso=float(input("Indique su ingreso: "))
anno_nac=int(input("Indique el año de nacimiento: "))
numero_hijos=int(input("Indique la cantidad de hijos que tiene: "))
annos_banco=int(input("Indique la cantidad de años en el banco: "))
estado_civ=str(input("Indique con la letra S si es soltero y C si es casado"))
camp_ciu=str(input("Indique con la letra U si vive en un sitio urbano y R si es rural"))

calculadora_edad = 2021 - anno_nac


if annos_banco >= 10 and numero_hijos >= 2:
  print("APROBADO")
else:
  if estado_civ == "C" and numero_hijos > 3 and calculadora_edad >= 45 and calculadora_edad <= 55:
    print("APROBADO")
  elif ingreso > 2500000 and estado_civ=="S" and camp_ciu=="U":
    print("APROBADO")
  elif ingreso > 3500000 and annos_banco > 5:
    print("APROBADO")
  elif camp_ciu=="R" and estado_civ=="C" and numero_hijos <= 2:
    print("APROBADO")
  else:
    print("RECHAZADO")      