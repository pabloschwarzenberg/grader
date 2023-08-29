#Conversión de Decimal a Binario

numero = eval(input("numero: "))

resultado = ""

while numero > 0:
    resto = numero % 2
    resultado = str(resto) + resultado
    numero = numero // 2
    print("resultado=",resultado, sep="")