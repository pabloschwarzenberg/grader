#Contestador de celular
def contestar_llamada(numero, hora):
  if hora >= 0 and hora <= 7:
    print("Contestar")
  elif hora < 14 and numero % 1000 == 909:
    print("Contestar")
  elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
    print("Contestar")
  else:
    print("No contestar")

numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

resultado = contestar_llamada(numero, hora)