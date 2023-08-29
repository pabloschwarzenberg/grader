#Conversión de Decimal a Binario
#Solicitar el numero decimal al usuario
numero_decimal = int(input("Ingrese un numero decimal: "))

#Realizar la conversion 
numero_binario = ""
while numero_decimal > 0:
    residuo = numero_decimal % 2
    numero_binario = str(residuo) + numero_binario
    numero_decimal = numero_decimal // 2

#resultado
print("resultado =", numero_binario)     
      