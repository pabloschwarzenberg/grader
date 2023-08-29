#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese el RUT sin dígito verificador: "))
digito_verificador = 0
def calcular_digito_verificador(rut):
  rut_str = str(rut)
  rut_reverso = rut_str[::-1]
  multiplicador = 2
  suma = 0
  for digito in rut_reverso:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
      multiplicador = 2
  resto = suma % 11
  digito_verificador = 11 - resto
  if digito_verificador == 11:
    return "dv=0"
  elif digito_verificador == 10:
    return "dv=K"
  else:
    return "dv=" + str(digito_verificador)

resultado = calcular_digito_verificador(rut)
print(resultado)
