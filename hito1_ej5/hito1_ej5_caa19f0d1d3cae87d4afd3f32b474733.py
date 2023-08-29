def Calculo_del_digito_verificador(rut):
  rut = str(rut)
  rut = rut.zfill(8)
  m = 2
  suma = 0
  for i in range(7, -1, -1):
    digito = int(rut[i])
    suma += m * digito
    m += 1
    if m == 8:
      m = 2
  digito_verificador = 11 - (suma % 11)
  if digito_verificador == 11:
    digito_verificador = 0
  elif digito_verificador == 10:
    digito_verificador = "K"
  return digito_verificador
  
Numero_de_rut = input("Ingrese el numero del rut(sin punto ni guion):")
digito_verificador = Calculo_del_digito_verificador(Numero_de_rut)
print("dv="  + str(digito_verificador))