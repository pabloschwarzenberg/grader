#Conversión de Decimal a Binario
#Definir la funcion decimal_a_binario
def decimal_a_binario(numero_decimal):
 numero_binario=0
 multiplicador=1

#Si el numero es diferente de 0
 while numero_decimal!=0:
  numero_binario=numero_binario+(numero_decimal%2)*multiplicador
  numero_decimal//=2
  multiplicador=multiplicador*10
 return numero_binario

#Pedir al usuario el numero que desea transformar
numero_decimal=float(input("Ingrese el numero decimal que desa transformar a binario: "))
numero_binario=decimal_a_binario(numero_decimal)

print("Resultado= ", numero_binario)      