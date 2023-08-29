#Contestador de celular
numero = int(input("Ingrese numero telefonico:"))
hora = int(input("Ingrese la hora de llamada:"))
      
if hora >= 0 and hora <= 7:
  Resultado = "CONTESTAR"
elif hora < 14 and numero % 100 == 9:
  Resultado = "CONTESTAR"
elif hora  >= 17 and hora <= 19 and numero // 1000000 == 877:
  Resultado  = "NO CONTESTAR"
elif hora >= 19:
  Resultado = "NO CONTESTAR"
else:
  Resultado = "NO CONTESTAR"
      
print("Resultado", Resultado)