#Contestador de celular
Numero = int(input("Ingrese Numero :"))
Hora = int(input("Ingreso Hora de la llamada"))
Numero = str(Numero)

if (Hora == 0 or Hora <= 7):
    Resultado = "CONTESTAR"
elif (Hora < 14) and (Numero.endswith("909") == True):
    Resultado = "CONTESTAR"
elif (Hora < 14):
    Resultado = "NO CONTESTAR"
elif (Hora >= 17 or Hora <=19) and (Numero.startswith("877") == True):
    Resultado = "NO CONTESTAR"
elif (Hora == 17 or Hora <=19):
    Resultado = "CONTESTAR"
else :
    Resultado = "NO CONTESTAR"
print(Resultado)