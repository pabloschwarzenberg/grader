#conversionde decimal a binario 
numero = int(input('escriba un numero: '))
cadena = ''
while numero // 2 != 0:
    cadena = str(numero % 2) + cadena
    numero = numero // 2
binario = (str(numero) + cadena)
print("resultado=", int(binario))