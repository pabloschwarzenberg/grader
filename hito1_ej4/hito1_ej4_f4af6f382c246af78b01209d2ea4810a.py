#Conversión de Decimal a Binario

decimal = int(input())

resultado = 0
ponderacion = 1

if decimal == 0:
    resultado = 0
if decimal == 1:
    resultado = 1
    
while decimal > 1:
    resultado = resultado + (ponderacion * (decimal%2))
    decimal = round((decimal // 2))
    ponderacion = ponderacion * 10
    if decimal == 1:
        resultado = resultado + ponderacion
    
print("resultado=",resultado)