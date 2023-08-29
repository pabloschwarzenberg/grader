numero=(int(input("Ingrese número de teléfono:")))
hora=(int(input("ingrese hora de llamada:")))
numero = str(numero)
if (hora == 0 or hora <= 7):
  resultado = "CONTESTAR"
if (hora < 14 and numero.endswith("909") == True):
  resultado= "CONTESTAR"
elif (hora<14):
  resultado= "NO CONTESTAR"
elif (hora >=17 or hora <=19) and (numero.startswith("877") == True):
  resultado= "NO CONTESTAR"
elif (hora ==17 or hora <=19):
  resultado= "CONTESTAR"
else:
  resultado = "NO CONTESTAR"
print(resultado)
