#Contestador de celular

numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
resultado = ""

if(hora >= 0 and hora <= 7):
  resultado = "CONTESTAR"
if(hora > 7 and hora <= 14 and numero%1000 == 909):
  resultado = "CONTESTAR"
else:
  resultado = "NO CONTESTAR"
if(hora >= 17 and hora <= 19 and numero//100000 == 877):
  resultado = "NO CONTESTAR"
else:
  resultado ="CONTESTAR"
if(hora > 19):
  resultado = "NO CONTESTAR"
  
print(resultado)