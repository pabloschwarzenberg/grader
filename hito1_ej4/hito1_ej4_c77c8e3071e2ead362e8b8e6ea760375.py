#Conversión de Decimal a Binario
numero_decimal = input("ingrese un numero")

modulos = [] 

while numero_decimal != 0:
    modulo = numero_decimal % 2
    cociente = numero_decimal // 2
    modulos.append(modulo) 
    numero_decimal = cociente 

print(modulos)