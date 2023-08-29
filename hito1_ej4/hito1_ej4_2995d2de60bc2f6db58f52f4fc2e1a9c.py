#Conversión de Decimal a Binario
def decimal_a_binario(x):
x= int(input("ingrese numero decimal: ")
if x== 0: 
  return""
else:
return decimal_a_binario(x/2)+ str(x%2)
