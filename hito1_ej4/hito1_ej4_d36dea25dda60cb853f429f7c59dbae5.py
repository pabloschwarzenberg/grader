#Conversión de Decimal a Binario
nro_decimal = int(input("Ingrese un número decimal: "))
if nro_decimal == 0:
    print(0)
nro_binario = ""
while nro_decimal > 0:
    nro_binario1 = nro_decimal % 2
    nro_binario = str(nro_binario1) + nro_binario
    nro_decimal = nro_decimal // 2
print("resultado="+nro_binario)    