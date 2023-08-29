#Contestador de celular

# Lo leemos como string para usar el metodo startswith y endswith
num = input("Número de teléfono: ")
hora = int(input("Hora del día: "))

if 0 <= hora <= 7:
  print("Resultado: CONTESTAR")
elif hora <= 14:
  if num.endswith("909"):
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif 17 <= hora <= 19:
  if num.startswith("877"):
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")
elif 19 <= hora:
  print("Resultado: NO CONTESTAR")
