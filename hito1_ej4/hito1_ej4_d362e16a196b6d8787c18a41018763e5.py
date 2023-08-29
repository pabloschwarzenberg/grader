var_decimal=int(input("Ingresa numero decimal:"))
var_binario=''
while var_decimal > 0:
  var_resto = int(var_decimal % 2)
  var_decimal = int(var_decimal / 2)
  var_binario = str(var_resto) + var_binario

print("el numero binario es :",var_binario)