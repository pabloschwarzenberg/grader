#Conversión de Decimal a Binario
numero_decimal = int(input("ingrese numero decimal :"))
lista = []
while numero_decimal>0:
   restos = int(numero_decimal%2)
   lista.append(restos)
   numero_decimal = (numero_decimal-restos)/2
numero_binario_final = ""
for e in lista[: :-1]:
  numero_binario_final = numero_binario_final + str(e)
  print("resultado="+str(numero_binario_final))
